%include ('./view/bsfiles/view/html_hdr.tpl')

%include ('./view/bsfiles/view/navbar.tpl')

    <div class="container-fluid">
      <div class="row">
      	%include ('./view/bsfiles/view/nav_sidebar.tpl')
      	<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
      	  <h3 class="sub-header">数据查询（内部使用）</h3>
      	  <table class="table table-striped">
      	  	<tbody>
	      	  <form action="/query" method="POST">
	      	  	<tr>
	      	  	  <td>
		      	  	  <label class="col-sm-4 control-label">开始时间</label>
		      	  	  <div class="col-sm-6">
		        	  	<input type="text" class="form-control input-sm" id="startdate" name="startdate" 
		        	  	placeholder="2015-01-30 15:55:06"/>
		        	  </div>
		          </td>
		          <td>
		      	  	  <label class="col-sm-4 control-label">结束时间</label>
		      	  	  <div class="col-sm-6">
		        	  	<input type="text" class="form-control input-sm" id="enddate" name="enddate" 
		        	  	placeholder="2015-01-30 15:55:07"/>
		        	  </div>
		          </td>
	      	  	  <td>
		      	  	  <label class="col-sm-4 control-label">超限状态</label>
		      	  	  <div class="col-sm-6">
		        	  <select class="form-control input-sm" name="smState">
	        			<option value="超限">超限</option>
	        			<option value="正常">正常</option>
	        			<option value="" selected>全部</option>
		        	  </select>
		        	  </div>
		          </td>
		        </tr>
		        <tr>
		          <td>
		        	  <label class="col-sm-4 control-label">处理状态</label>
		        	  <div class="col-sm-6">
		        	  <select class="form-control input-sm" name="ReadFlag">
		        	  	<opton value="None">未处理</option>
	        			<option value="1">已申请处理</option>
	        			<option value="2">处理申请已审核</option>
	        			<option value="3">处理已登记</option>
	        			<option value="4">处理登记已审核</option>
	        			<option value="" selected>全部</option>
		        	  </select>
		        	  </div>
	        	  </td>
	        	  <td>
		        	  <label class="col-sm-4 control-label">站点编号</label>
		        	  <div class="col-sm-6">
		        	  <select class="form-control input-sm" name="SiteID" id="siteid">
		        	  	%for i in xrange(1, 9):
	        			<option value={{i}}>{{i}}</option>
	        			%end
	        			<option value="" selected>全部</option>
		        	  </select>
		        	  </div>
	        	  </td>
	        	  <td>
		        	  <label class="col-sm-4 control-label">车轴数</label>
		        	  <div class="col-sm-6">
		        	  <select class="form-control input-sm" name="smWheelCount" id="wheels">
		        	  	%for i in xrange(2, 7):
	        			<option value="{{i}}">{{i}}</option>
	        			%end
	        			<option value="" selected>全部</option>
		        	  </select>
		        	  </div>
	        	  </td>
	        	</tr>
	        	<tr>
	        		<td>
		        	  <label class="col-sm-4 control-label">车牌号</label>
		        	  <div class="col-sm-6">
		        	  	<input type="text" class="form-control input-sm" name="VehicheCard"/>
		        	  </div>
	        	  	</td>
	        	  	<td>
		        	  <label class="col-sm-4 control-label">超限率</label>
		        	  <div class="col-sm-6">
		        	  	<!--input type="text" class="form-control input-sm" name="smLimitWeightPercent"/-->
		        	  	<select class="form-control input-sm" name="smLimitWeightPercent" id="smLimitWeightPercent">
		        	  	%for i in xrange(10, 110, 10):
	        			<option value="{{i}}">{{i}}</option>
	        			%end
	        			<option value="" selected>全部</option>
		        	  	</select>
		        	  </div>
	        	  	</td>
	        	  	<td>
		        	  <label class="col-sm-4 control-label">车重</label>
		        	  <div class="col-sm-6">
		        	  	<input type="text" class="form-control input-sm" name="smTotalWeight"/>
		        	  </div>
	        	  	</td>
	        	</tr>
	        	<tr>
	        	  <td>
	        		<button type="submit" class="btn btn-md btn-primary" name="query" value="show">查询</button>
	        	  </td>
	        	</tr>
	          </form>
	        </tbody>
          </table>
          %if results is not None:
          	<h3 class="sub-header">数据查询结果</h3>
	        <table class="table table-striped">  
	          <thead>
	          	<tr>
	          	  %for col in results[0]:
	          	    <th>{{col}}</th>
	          	  %end
	          	  <th>操作</th>
	          	</tr>
	          </thead>
	          <tbody>
	          	%for res in details[1:]:
	          	  <tr>
	          	  %for col in res[0]:
	          	    <td>{{col}}</td>
	          	  %end
	          	  <td>
	          	  	<button type="button" class="btn btn-sm btn-primary" data-toggle="modal" 
	          	  			data-target="#rec-modula-{{res[1][0]}}">
	          	  		查看详情
	          	  	</button>
	          	  	%include ('./view/bsfiles/view/query_modula.tpl', seq=res[1][0])
	          	  </td>
	          	  </tr>
	          	%end
	          </tbody>
	        </table>
	      %end
    	</div>
      </div>
  	</div>

	<!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/view/bsfiles/js/jquery.min.js"></script>
    <script src="/static/view/bsfiles/js/bootstrap.min.js"></script>

%include ('./view/bsfiles/view/html_footer.tpl')