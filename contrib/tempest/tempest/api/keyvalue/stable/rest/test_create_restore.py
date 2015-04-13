# Copyright 2014 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import uuid

from tempest.api.keyvalue.rest_base.base import MagnetoDBTestCase
from tempest_lib.common.utils.data_utils import rand_name


class MagnetoDBCreateRestoreTest(MagnetoDBTestCase):
    def setUp(self):
        super(MagnetoDBCreateRestoreTest, self).setUp()
        self.tname = rand_name(self.table_prefix).replace('-', '')

    def test_create_restore_job(self):
        self._create_test_table(self.smoke_attrs,
                                self.tname,
                                self.smoke_schema,
                                wait_for_active=True)

        backup_uuid = uuid.uuid4()

        headers, body = self.management_client.create_restore_job(
            self.tname, backup_uuid.hex)
        self.assertEqual(self.tname, body['table_name'])
        self.assertEqual('RESTORING', body['status'])
