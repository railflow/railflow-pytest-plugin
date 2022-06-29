import json
import re
import warnings
from collections import OrderedDict
from datetime import datetime

import pytest

CLASS_KEYS = ['railflow_test_attributes', 'class_name', 'file_name']
CLASS_ONLY = ['class_railflow', 'class_markers']

_py_ext_re = re.compile(r"\.py$")


def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
    return "%s:%s: %s:%s\n" % (filename, lineno, category.__name__, message)


warnings.formatwarning = warning_on_one_line


def pytest_addoption(parser):
    """
    Adds commandline option for creating the json file.
    """
    group = parser.getgroup("Json report")
    group.addoption(
        "--jsonfile",
        action="store",
        dest="jsonpath",
        default=None,
        help="name of the json file where test details are saved.",
    )


def pytest_configure(config):
    """
    Adds jsonpath to pytest config and additional markers to pytest ini.
    """
    jsonpath = config.option.jsonpath
    if jsonpath:
        config.json = JiraJsonReport(jsonpath)
        config.pluginmanager.register(config.json)
    # register an additional marker
    config.addinivalue_line(
        "markers", "railflow(options): read custom metadata")


def pytest_unconfigure(config):
    json = getattr(config, "json", None)
    if json:
        del config.json
        config.pluginmanager.unregister(json)


def mangle_test_address(address):
    """Split and modify test address to required format"""
    path, _, _ = address.partition("[")
    names = path.split("::")
    try:
        names.remove("()")
    except ValueError:
        pass

    names[0] = names[0].replace("/", ".")
    names[0] = _py_ext_re.sub("", names[0])
    # names[-1] += brack + params
    return names


def is_custom_attr_name_value_pairs(custom_attrs):
    # Check if it is a list
    if isinstance(custom_attrs, list):
        # loop through values
        for custom_attr in custom_attrs:
            # ensure it is a key, value pair
            if not isinstance(custom_attr, dict):
                break
            # ensure only 2 keys
            if len(custom_attr) != 2:
                break
            # ensure keys are 'name' and 'value'
            if custom_attr.get('name', None) is None or \
                    custom_attr.get('value', None) is None:
                break
        else:
            # If the loop never breaks then that means every attribute is a valid format
            return True
    # if any condition fails, we will return False here
    return False


def restructure(data):
    restructured_list = []
    restructured_classes = {}
    temp_list = []

    for entry in data:
        if isinstance(entry, OrderedDict):
            class_name = entry.get('class_name', None)

            identifier = '{}{}:{}'.format(
                entry['file_name'],
                ".{}".format(entry['class_name']) if entry['class_name'] is not None else "",
                entry['test_name']
            )
            formatted_test = {}

            for entry_key in entry:
                if (class_name is None or entry_key not in CLASS_KEYS) and \
                        entry_key not in CLASS_ONLY:
                    formatted_test[entry_key] = entry[entry_key]
            if len(temp_list) > 0:
                formatted_test['railflow_test_attributes'] = OrderedDict(temp_list)

            if class_name is not None:
                formatted_entry = restructured_classes.get(identifier.split(':')[0], None)
                if formatted_entry is None:
                    formatted_entry = {
                        'class_name': entry['class_name'],
                        'markers': entry['class_markers'],
                        'file_name': entry['file_name'],
                        'tests': [],
                    }
                    if len(entry['class_railflow']) > 0:
                        formatted_entry['railflow_test_attributes'] = OrderedDict(
                            entry['class_railflow'])
                formatted_entry['tests'].append(formatted_test)
                # if entry.get('attachments', None) is not None:
                #     formatted_entry['attachments'] += entry['attachments']
                restructured_classes[identifier.split(':')[0]] = formatted_entry
            else:
                restructured_list.append(formatted_test)
            temp_list = []
        else:
            temp_list.append(entry)

    for _, restructured_class in restructured_classes.items():
        restructured_list.append(restructured_class)

    return restructured_list


class JiraJsonReport(object):
    """
    Creates Json report
    """

    def __init__(self, jsonpath):
        self.results = []
        self.jsonpath = jsonpath
        self.screenshots = {}
        self.test_steps = {}
        self.extra = {}
        self.class_list = [
            "case_fields",
            "result_fields",
            "case_type",
            "case_priority",
            "smart_failure_assignment",
        ]
        self.fun_list = [
            "jira_ids",
            "case_fields",
            "result_fields",
            "testrail_ids",
            "case_type",
            "case_priority",
        ]

    @pytest.fixture()
    def testrail_add_screenshot(self, request):
        def _func(path):
            current = self.screenshots.get(request.node.nodeid, [])
            current.append(path)
            self.screenshots[request.node.nodeid] = current

        yield _func

    @pytest.fixture()
    def testrail_add_test_step(self, request):
        def _func(name, status, actual_val="", expected_val=""):
            test_step = {
                "step_name": str(name),
                "status": str(status),
                "actual": str(actual_val),
                "expected": str(expected_val)
            }
            current = self.test_steps.get(request.node.nodeid, [])
            current.append(test_step)
            self.test_steps[request.node.nodeid] = current

        yield _func

    def append(self, result):
        self.results.append(result)

    def build_result(self, report, status, message):
        """
        Builds test results
        """
        result = OrderedDict()
        names = mangle_test_address(report.nodeid)
        fname = report.location[0].split(".")[0]
        if names[-2].split(".")[-1] != fname.split("/")[-1]:
            result["class_name"] = names[-2]
        else:
            result["class_name"] = None
        result["test_name"] = names[-1]
        if report.test_doc is None:
            result["details"] = report.test_doc
        else:
            result["details"] = report.test_doc.strip()
        result["markers"] = report.test_marker
        result["class_markers"] = report.class_marker
        result["class_railflow"] = report.class_railflow
        if len(report.test_params) > 0:
            result["parameters"] = report.test_params
        result["result"] = status
        result["duration"] = getattr(report, "duration", 0.0)
        result["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        result["message"] = str(message) if message is not None else None
        result["file_name"] = fname.split("/")[-1]
        if hasattr(report.longrepr, "reprtraceback"):
            self.extra[result["file_name"]] = report.longrepr.reprtraceback
        result["test_steps"] = self.test_steps.get(report.nodeid, [])
        result["attachments"] = self.screenshots.get(report.nodeid, [])
        self.append(result)

    def append_pass(self, report):

        status = "PASSED"
        message = None
        self.build_result(report, status, message)

    def append_failure(self, report):

        if hasattr(report, "wasxfail"):
            status = "XPASSED"
            message = "xfail-marked test passes Reason: %s " % report.wasxfail

        else:
            message = str(report.longrepr)
            status = "FAILED"

        self.build_result(report, status, message)

    def append_error(self, report):

        message = report.longrepr
        status = "ERROR"
        self.build_result(report, status, message)

    def append_skipped(self, report):

        if hasattr(report, "wasxfail"):
            status = "XFAILED"
            message = "expected test failure Reason: %s " % report.wasxfail

        else:
            status = "SKIPPED"
            _, _, message = report.longrepr
            if message.startswith("Skipped: "):
                message = message[9:]

        self.build_result(report, status, message)

    @pytest.hookimpl(tryfirst=True)
    def pytest_collection_modifyitems(self, items):
        # Custom attribute types
        attr_types = {
            'title': {
                "validation": lambda val: isinstance(val, str),
                "expected": "String (i.e. 'My Foo')"
            },
            'case_fields': {
                "validation": is_custom_attr_name_value_pairs,
                "expected": "list of Name value pairs (i.e. [{'name': 'Foo', 'value': 2312}, "
                            "{'name': 'Bar', 'value': 'Baz'}])"
            },
            'result_fields': {
                "validation": is_custom_attr_name_value_pairs,
                "expected": "list of Name value pairs (i.e. [{'name': 'Foo', 'value': 2312}, "
                            "{'name': 'Bar', 'value': 'Baz'}])"
            },
            'case_type': {
                "validation": lambda val: isinstance(val, str),
                "expected": "String (i.e. 'Automated')"
            },
            'case_priority': {
                "validation": lambda val: isinstance(val, str),
                "expected": "String (i.e. 'High')"
            },
            'testrail_ids': {
                "validation": lambda val: isinstance(val, list) and
                [isinstance(v, int) for v in val].count(True) == len(val),
                "expected": "List of intergers (i.e. [1, 2, 456, 7, 3])"
            },
            'jira_ids': {
                "validation": lambda val: isinstance(val, list) and
                [isinstance(v, str) for v in val].count(True) == len(val),
                "expected": "List of strings (i.e. ['FOO-1', 'BAR-1', 'BAZ-56'])"
            },
            'smart_failure_assignment': {
                "validation": lambda val: isinstance(val, list) and
                [isinstance(v, str) for v in val].count(True) == len(val),
                "expected": "List of strings (i.e. ['jdoe', 'jimbo'])"
            }
        }
        # Check every collected test
        for test_item in items:
            # Check each mark
            for test_mark in test_item.iter_markers():
                # if it is a testrail mark
                if test_mark.name == 'railflow':
                    # Check each attribute on the test
                    for custom_attr_name in test_mark.kwargs:
                        # Get the validation function for the given metric
                        attr_val_obj = attr_types.get(custom_attr_name, None)
                        identifier = '{}{}:{}'.format(
                            test_item.module.__name__,
                            ".{}".format(test_item.cls.__name__) if test_item.cls is not None
                            else "",
                            test_item.name
                        )
                        # If there is no function (invalid attribute) or
                        # the validation fails, raise an error
                        if attr_val_obj is None:
                            raise ValueError('{} - Attribute "{}" is not a valid \
                                Railflow attribute'.format(identifier, custom_attr_name))
                        if not attr_val_obj['validation'](test_mark.kwargs[custom_attr_name]):
                            raise ValueError(
                                '{} - Railflow attribute "{}" has an invalid value of '
                                '{}, expected: {}'.format(
                                    identifier,
                                    custom_attr_name,
                                    test_mark.kwargs[custom_attr_name],
                                    attr_val_obj['expected']))

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(self, item, call):
        """
        pytest hook that creates a test report for each of the setup, call,
        and teardown phases of a test
        """

        # Wait to look at results until after pytests processing
        outcome = yield

        test_result = outcome.get_result()
        test_result.test_doc = item.obj.__doc__
        class_marker = []
        class_railflow = []
        test_marker = []
        test_params = []

        # Get all the test marks
        marks = item.own_markers
        if marks is not None:
            for mark in marks:
                if mark.name != "railflow":
                    test_marker.append(mark.name)
                    # Extract parameters if they exist
                    if mark.name == 'parametrize':
                        for param_var in mark.args[0].split(','):
                            test_params.append({
                                'name': param_var,
                                'value': item.funcargs[param_var]
                            })
        test_result.test_marker = ", ".join(test_marker)

        # Get all the class markes
        if item.cls is not None and hasattr(item.cls, 'pytestmark') and len(item.cls.pytestmark):
            for mark in item.cls.pytestmark:
                if mark.name != 'railflow':
                    class_marker.append(mark.name)
        test_result.class_marker = ", ".join(class_marker)

        test_result.test_params = test_params

        failed_in_setup = test_result.when == "setup" and test_result.outcome != 'passed'

        if (test_result.when == "call" or failed_in_setup) and marks is not None:
            for mark in reversed(marks):
                for mark_arg in mark.kwargs:
                    self.results.append((mark_arg, mark.kwargs[mark_arg]))

            if item.cls is not None and hasattr(item.cls, 'pytestmark'):
                for mark in reversed(item.cls.pytestmark):
                    for mark_arg in mark.kwargs:
                        class_railflow.append((mark_arg, mark.kwargs[mark_arg]))

        test_result.class_railflow = class_railflow

    def pytest_runtest_logreport(self, report):

        if report.passed:
            if report.when == "call":
                self.append_pass(report)

        elif report.failed:
            if report.when == "call":
                self.append_failure(report)

            else:
                self.append_error(report)

        elif report.skipped:
            self.append_skipped(report)

    def pytest_sessionfinish(self, session):
        if not hasattr(session.config, "slaveinput"):
            if self.results:
                for k, v in self.extra.items():
                    out = str(v)
                    start = out.find("png: ") + len("png: ")
                    end = out.find("\nhtml:")
                    for i in range(len(self.results)):
                        if isinstance(self.results[i], tuple):
                            continue
                        if self.results[i]["file_name"] == k:
                            if (
                                    self.results[i]["result"] == "FAILED"
                                    or self.results[i]["result"] == "XFAILED"
                            ):
                                if ".png" in out:
                                    attachments = self.results[i].get("attachments", [])
                                    attachments.append(out[start:end])
                                    self.results[i]['attachments'] = attachments

                fieldnames = restructure(self.results)

                if self.jsonpath:
                    filepath = self.jsonpath
                    with open(filepath, "w") as file:
                        json.dump(
                            fieldnames,
                            file,
                            sort_keys=False,
                            indent=4,
                            separators=(",", ": "),
                        )

    def pytest_terminal_summary(self, terminalreporter):
        if self.results:
            terminalreporter.write_sep(
                "-*", "Json report written to %s" % self.jsonpath
            )
        else:
            terminalreporter.write_sep("-*", "No Json report is created.")
