%include ('./view/bsfiles/view/html_hdr.tpl')

%include ('./view/bsfiles/view/navbar.tpl')

    <div class="container-fluid">
      <div class="row">
      	%include ('./view/bsfiles/view/nav_sidebar.tpl')
      	<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
      	  <h3 class="sub-header">超限处理</h3>
      	  <table class="table table-striped">
      	  	<tbody>
	      	  <form action="/proceed_query" method="POST">
	      	  	<tr>
	      	  	  <td>
		      	  	  <label class="col-sm-4 control-label">开始时间</label>
		      	  	  <div class="col-sm-4">
		        	  	...
		        	  </div>
		          </td>
		        </tr>
		        <tr>
		          <td>
		        	  <label class="col-sm-4 control-label">处理状态</label>
		        	  <div class="col-sm-4">
		        	  <select class="form-control input-sm" name="proceeded" id="proceeded">
	        			<option value="yes">已处理</option>
	        			<option value="no">未处理</option>
	        			<option value="" selected>全部</option>
		        	  </select>
		        	  </div>
	        	  </td>
	        	  <td>
		        	  <label class="col-sm-4 control-label">站点编号</label>
		        	  <div class="col-sm-4">
		        	  <select class="form-control input-sm" name="siteid" id="siteid">
		        	  	%for i in xrange(1, 9):
	        			<option value={{i}}>{{i}}</option>
	        			%end
	        			<option value="" selected>全部</option>
		        	  </select>
		        	  </div>
	        	  </td>
	        	  <td>
		        	  <label class="col-sm-4 control-label">车轴数</label>
		        	  <div class="col-sm-4">
		        	  <select class="form-control input-sm" name="wheels" id="wheels">
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
	          	%for res in results[1:]:
	          	  <tr>
	          	  %for col in res:
	          	    <td>{{col}}</td>
	          	  %end
	          	  <td>
	          	  	<button type="button" class="btn btn-sm btn-primary" data-toggle="modal" data-target="#rec-modula">
	          	  		查看详情
	          	  	</button>
	          	  	<button type="button" class="btn btn-sm btn-primary" formaction="/proceed" formmethod="post" 
	          	  			name="proceed" value="go">
	          	  		申请处理
	          	  	</button>
	          	  	%include ('./view/bsfiles/view/query_modula.tpl', detail=details[results.index(res)])
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