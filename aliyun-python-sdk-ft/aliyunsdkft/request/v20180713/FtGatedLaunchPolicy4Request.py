# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class FtGatedLaunchPolicy4Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2018-07-13', 'FtGatedLaunchPolicy4','serviceCode')

	def get_IsGatedLaunch(self):
		return self.get_query_params().get('IsGatedLaunch')

	def set_IsGatedLaunch(self,IsGatedLaunch):
		self.add_query_param('IsGatedLaunch',IsGatedLaunch)