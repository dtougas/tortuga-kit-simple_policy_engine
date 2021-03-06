#!/usr/bin/env python

# Copyright 2008-2018 Univa Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tortuga.rule.ruleCli import RuleCli


class GetRuleListCli(RuleCli):
    """
    Get rule list command line interface.

    """
    def runCommand(self):
        self.parseArgs(_("""
    get-rule-list [options]

Description:
    The get-rule-list tool returns the list of Tortuga Simple Policy Engine
    rules that are active in the system.  New rules can be added  with
    add-rule.
"""))

        rule_list = self.get_rule_api().getRuleList()
        for r in rule_list:
            print('{}'.format(r))


def main():
    GetRuleListCli().run()
