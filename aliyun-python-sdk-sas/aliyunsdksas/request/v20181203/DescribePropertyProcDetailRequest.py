# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class DescribePropertyProcDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribePropertyProcDetail','sas')

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_Uuid(self):
		return self.get_query_params().get('Uuid')

	def set_Uuid(self,Uuid):
		self.add_query_param('Uuid',Uuid)

	def get_Cmdline(self):
		return self.get_query_params().get('Cmdline')

	def set_Cmdline(self,Cmdline):
		self.add_query_param('Cmdline',Cmdline)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_User(self):
		return self.get_query_params().get('User')

	def set_User(self,User):
		self.add_query_param('User',User)