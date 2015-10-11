%include ('./view/bsfiles/view/html_hdr.tpl')

%include ('./view/bsfiles/view/navbar.tpl')

    <div class="container-fluid">
      <div class="row">
      	%include ('./view/bsfiles/view/nav_sidebar.tpl')
      	<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
      	  <h3 class="sub-header">超限处理</h3>
      	  <table class="table table-responsive">
      	  	<tbody>
	      	  <form action="/reg_approval" method="POST">
	      	  	<tr>
	      	  	  <td>
		      	  	  <label class="col-sm-4 control-label">开始时间</label>
		      	  	  <div class="col-sm-6">
		        	  	<input type="date" class="form-control input-sm" id="startdate" name="startdate" 
		        	  	placeholder="2015-01-30"/>
		        	  </div>
		          </td>
		          <td>
		      	  	  <label class="col-sm-4 control-label">结束时间</label>
		      	  	  <div class="col-sm-6">
		        	  	<input type="date" class="form-control input-sm" id="enddate" name="enddate" 
		        	  	placeholder="2015-01-30"/>
		        	  </div>
		          </td>
		        </tr>
		        <tr>
		          <td>
		        	  <label class="col-sm-4 control-label">处理状态</label>
		        	  <div class="col-sm-6">
		        	  <select class="form-control input-sm" name="ReadFlag" id="ReadFlag">
	        			<option value="2">待登记</option>
	        			<option value="3" selected>已登记待审核</option>
	        			<option value="4">登记已审核</option>
	        			<option value="">全部</option>
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
		        	  	<input type="text" class="form-control input-sm" name="smLimitWeightPercent"/>
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
	          	  	%if res[1][-1] == 3:
	          	  		<button class="btn btn-sm btn-primary" 
	          	  				onclick="alert('登记已审核!');location.href='/registered/{{res[1][0]}}';">
	          	  			登记审核通过
	          	  		</button>
	          	  	%end
	          	  	
	          	  	%include ('./view/bsfiles/view/query_modula.tpl')
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
    <script type="text/javascript">
	  $(function() {
	    $( "#startdate" ).datepicker();
	    $( "#enddate" ).datepicker();
	  });
	</script>

%include ('./view/bsfiles/view/html_footer.tpl')