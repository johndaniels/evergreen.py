from copy import deepcopy
from datetime import datetime, timedelta
import json

import pytest

from evergreen.task import Task, _EVG_DATE_FIELDS_IN_TASK

SAMPLE_TASK_DATA = json.loads("""
{
    "task_id": "mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16",
    "project_id": "mongodb-mongo-master",
    "create_time": "2019-02-13T14:55:37.000Z",
    "dispatch_time": "2019-02-13T19:33:20.590Z",
    "scheduled_time": "2019-02-13T19:12:26.067Z",
    "start_time": "2019-02-13T19:33:21.000Z",
    "finish_time": "2019-02-13T19:39:41.653Z",
    "ingest_time": "2019-02-13T19:03:21.000Z",
    "version_id": "5c6469b6d6d80a06ba7b3aff",
    "revision": "3a8290eef5c5934462b5cb84c9daded1b3073ad9",
    "priority": 0,
    "activated": true,
    "activated_by": "",
    "build_id": "mongodb_mongo_master_linux_64_debug_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16",
    "distro_id": "rhel62-large",
    "build_variant": "linux-64-debug",
    "depends_on": [ "mongodb_mongo_master_linux_64_debug_aggregation_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16"
    ],
    "display_name": "aggregation_auth",
    "host_id": "sir-eh3i5x3j",
    "restarts": 1,
    "execution": 1,
    "order": 762,
    "status": "success",
    "status_details": {
      "status": "success",
      "type": "setup",
      "desc": "'shell.exec' in \\"run tests\\"",
      "timed_out": false
    },
    "logs": {
      "all_log": "https://evergreen.mongodb.com/task_log_raw/mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16/0?type=ALL",
      "task_log": "https://evergreen.mongodb.com/task_log_raw/mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16/0?type=T",
      "agent_log": "https://evergreen.mongodb.com/task_log_raw/mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16/0?type=E",
      "system_log": "https://evergreen.mongodb.com/task_log_raw/mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16/0?type=S"
    },
    "time_taken_ms": 379965,
    "expected_duration_ms": 412346,
    "est_wait_to_start_ms": 0,
    "estimated_cost": 0.025272363425925926,
    "generate_task": false,
    "generated_by": "",
    "artifacts": [
      {
        "name": "Disk Stats - Execution 0",
        "url": "https://s3.amazonaws.com/mciuploads/mongodb-mongo-master/linux-64-debug/3a8290eef5c5934462b5cb84c9daded1b3073ad9/diskstats/mongo-diskstats-mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16-0.tgz",
        "visibility": "",
        "ignore_for_fetch": false
      },
      {
        "name": "System Resource Info - Execution 0",
        "url": "https://s3.amazonaws.com/mciuploads/mongodb-mongo-master/linux-64-debug/3a8290eef5c5934462b5cb84c9daded1b3073ad9/systemresourceinfo/mongo-system-resource-info-mongodb_mongo_master_linux_64_debug_aggregation_auth_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16-0.tgz",
        "visibility": "",
        "ignore_for_fetch": false
      }
    ],
    "display_only": false,
     "previous_executions": [
      {
        "task_id": "mongodb_mongo_master_linux_64_debug_sharding_auth_gen_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16_0",
        "project_id": "mongodb-mongo-master",
        "create_time": "2019-02-13T14:55:37.000Z",
        "dispatch_time": "2019-02-13T19:02:35.784Z",
        "scheduled_time": "2019-02-13T19:02:27.907Z",
        "start_time": "2019-02-13T19:02:36.625Z",
        "finish_time": "2019-02-13T19:04:13.060Z",
        "ingest_time": "2019-02-13T19:02:17.947Z",
        "version_id": "5c6469b6d6d80a06ba7b3aff",
        "revision": "3a8290eef5c5934462b5cb84c9daded1b3073ad9",
        "priority": 0,
        "activated": true,
        "activated_by": "",
        "build_id": "mongodb_mongo_master_linux_64_debug_patch_3a8290eef5c5934462b5cb84c9daded1b3073ad9_5c6469b6d6d80a06ba7b3aff_19_02_13_19_02_16",
        "distro_id": "rhel62-large",
        "build_variant": "linux-64-debug",
        "depends_on": null,
        "display_name": "sharding_auth_gen",
        "host_id": "sir-hy3r79jg",
        "restarts": 0,
        "execution": 0,
        "order": 762,
        "status": "success",
        "status_details": {
          "status": "success",
          "type": "system",
          "desc": "'generate.tasks' in \\"generate resmoke tasks\\"",
          "timed_out": false
        },
        "logs": {
          "all_log": null,
          "task_log": null,
          "agent_log": null,
          "system_log": null
        },
        "time_taken_ms": 96435,
        "expected_duration_ms": 83532,
        "est_wait_to_start_ms": 0,
        "estimated_cost": 0.006414118055555555,
        "generate_task": true,
        "generated_by": "",
        "artifacts": null,
        "display_only": false
      }
    ]
  }""")


class TestTask(object):
    def test_time_fields_return_time_objects(self):
        task = Task(SAMPLE_TASK_DATA)
        for date_field in _EVG_DATE_FIELDS_IN_TASK:
            assert isinstance(getattr(task, date_field), datetime)

    def test_getting_attributes(self):
        task = Task(SAMPLE_TASK_DATA)
        assert SAMPLE_TASK_DATA['task_id'] == task.task_id
        with pytest.raises(TypeError):
            task.not_really_an_attribute

    def test_status_attributes(self):
        task = Task(SAMPLE_TASK_DATA)
        assert task.is_success()
        assert not task.is_system_failure()
        assert not task.is_timeout()

    def test_bad_status_attributes(self):
        sample_json = deepcopy(SAMPLE_TASK_DATA)
        sample_json['status_details']['type'] = 'system'
        sample_json['status'] = 'failed'
        sample_json['status_details']['timed_out'] = True
        task = Task(sample_json)
        assert not task.is_success()
        assert task.is_system_failure()
        assert task.is_timeout()

    def test_wait_time(self):
        task = Task(SAMPLE_TASK_DATA)
        assert timedelta(minutes=30) == task.wait_time()

    def test_missing_wait_time(self):
        sample_json = deepcopy(SAMPLE_TASK_DATA)
        sample_json['start_time'] = None
        task = Task(sample_json)
        assert not task.wait_time()

    def test_get_execution(self):
        task = Task(SAMPLE_TASK_DATA)
        execution1 = task.get_execution(1)
        assert execution1.display_name == 'aggregation_auth'

        execution0 = task.get_execution(0)
        assert execution0.display_name == 'sharding_auth_gen'

        assert not task.get_execution(999)
