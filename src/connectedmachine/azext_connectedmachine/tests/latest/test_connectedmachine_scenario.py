# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if, calc_coverage
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))
CUSTOM_SCRIPT_EXTENSION_NAME = 'customScript'
DEPENDENCY_AGENT_EXTENSION_NAME = 'dependencyAgent'

# Constants for Machine tests
MACHINES_RESOURCE_GROUP_NAME = 'AzcmagentTest'
MACHINES_MACHINE_NAME = '0.10.20225.002'
MACHINES_LOCATION = 'eastus2euap'

# Constants for Machine Extension tests
EXTENSIONS_RESOURCE_GROUP_NAME = 'csharp-sdk-test'
EXTENSIONS_MACHINE_NAME = 'thinkpad'
EXTENSIONS_LOCATION = 'eastus'

@try_manual
def setup(test):
    pass

@try_manual
def cleanup(test):
    pass

# Machine tests

# EXAMPLE: /Machines/get/Get Machine
@try_manual
def step__machines_get_get_machine(test):
    test.cmd('az connectedmachine machine show '
             f'--name "{MACHINES_MACHINE_NAME}" '
             f'--resource-group "{MACHINES_RESOURCE_GROUP_NAME}"',
             checks=[
                 test.check('name', MACHINES_MACHINE_NAME),
                 test.check('location', MACHINES_LOCATION)
             ])

# EXAMPLE: /Machines/get/List Machines by resource group
@try_manual
def step__machines_get_list_machines_by_resource_group(test):
    test.cmd('az connectedmachine machine list '
             f'--resource-group "{MACHINES_RESOURCE_GROUP_NAME}"',
             checks=[
                 test.greater_than('length(@)', 400)
             ])

# EXAMPLE: /Machines/delete/Delete a Machine
# @try_manual
# def step__machines_delete_delete_a_machine(test):
#     test.cmd('az connectedmachine machine delete -y '
#              '--name "{MACHINES_MACHINE_NAME}" '
#              '--resource-group "{MACHINES_RESOURCE_GROUP_NAME}"',
#              checks=[])

# # Machine Extension tests

# # EXAMPLE: /MachineExtensions/put/Create or Update a Machine Extension
# @try_manual
# def step__machineextensions_put(test):
#     test.cmd('az connectedmachine machine-extension create '
#              '--machine-name "{EXTENSIONS_MACHINE_NAME}" '
#              '--name "{CUSTOM_SCRIPT_EXTENSION_NAME}" '
#              '--EXTENSIONS_LOCATION "{EXTENSIONS_LOCATION}" '
#              '--type "CustomScriptExtension" '
#              '--publisher "Microsoft.Compute" '
#              '--settings "{{\\"commandToExecute\\":\\"powershell.exe -c \\\\\\"Get-Process | Where-Object {{ $_.CPU '
#              '-gt 10000 }}\\\\\\"\\"}}" '
#              '--type-handler-version "1.10" '
#              '--resource-group "{EXTENSIONS_RESOURCE_GROUP_NAME}"',
#              checks=[])

# # EXAMPLE: /MachineExtensions/get/GET Machine Extension
# @try_manual
# def step__machineextensions_get_get_machine_extension(test):
#     test.cmd('az connectedmachine machine-extension show '
#              '--machine-name "{EXTENSIONS_MACHINE_NAME}" '
#              '--name "{CUSTOM_SCRIPT_EXTENSION_NAME}" '
#              '--resource-group "{EXTENSIONS_RESOURCE_GROUP_NAME}"',
#              checks=[])

# # EXAMPLE: /MachineExtensions/get/GET all Machine Extensions
# @try_manual
# def step__machineextensions_get(test):
#     test.cmd('az connectedmachine machine-extension list '
#              '--machine-name "{EXTENSIONS_MACHINE_NAME}" '
#              '--resource-group "{EXTENSIONS_RESOURCE_GROUP_NAME}"',
#              checks=[])

# # EXAMPLE: /MachineExtensions/patch/Create or Update a Machine Extension
# @try_manual
# def step__machineextensions_patch(test):
#     test.cmd('az connectedmachine machine-extension update '
#              '--machine-name "{EXTENSIONS_MACHINE_NAME}" '
#              '--name "{CUSTOM_SCRIPT_EXTENSION_NAME}" '
#              '--type "CustomScriptExtension" '
#              '--publisher "Microsoft.Compute" '
#              '--settings "{{\\"commandToExecute\\":\\"powershell.exe -c \\\\\\"Get-Process | Where-Object {{ $_.CPU '
#              '-lt 100 }}\\\\\\"\\"}}" '
#              '--type-handler-version "1.10" '
#              '--resource-group "{EXTENSIONS_RESOURCE_GROUP_NAME}"',
#              checks=[])

# # EXAMPLE: /MachineExtensions/delete/Delete a Machine Extension
# @try_manual
# def step__machineextensions_delete(test):
#     test.cmd('az connectedmachine machine-extension delete -y '
#              '--machine-name "{EXTENSIONS_MACHINE_NAME}" '
#              '--name "MMA" '
#              '--resource-group "{EXTENSIONS_RESOURCE_GROUP_NAME}"',
#              checks=[])

@try_manual
def call_scenario(test):
    setup(test)
    print(MACHINES_MACHINE_NAME)
    # Machines
    step__machines_get_get_machine(test)
    step__machines_get_list_machines_by_resource_group(test)
    step__machines_get_list_machines_by_resource_group(test)
    # step__machines_delete_delete_a_machine(test)

    # # Machine Extensions
    # step__machineextensions_put(test)
    # step__machineextensions_get_get_machine_extension(test)
    # step__machineextensions_get(test)
    # step__machineextensions_patch(test)
    # step__machineextensions_delete(test)

    cleanup(test)


@try_manual
class ConnectedMachineScenarioTest(ScenarioTest):

    def test_connectedmachine(self):
        print(MACHINES_MACHINE_NAME)
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
