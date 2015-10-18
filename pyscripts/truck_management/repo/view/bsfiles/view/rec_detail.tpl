%include ('./view/bsfiles/view/html_hdr.tpl')
<div class="panel {{panel_type}}">
  <div class="panel-heading">
    <h3 class="panel-title">记录详情</h3>
  </div>
  <div class="panel-body">
    <ul class="list-group">
	    %for i in xrange(0, length, 1):
	    	%if (i==4 or i==10) and "danger" in panel_type:
	    	<li class="list-group-item list-group-item-danger">
	    	%else:
	    	<li class="list-group-item list-group-item-info">
	    	%end
	    		<tr><td>
					<label>{{detail[0][i]}}:&nbsp</label>
    		    	<span>{{detail[1][i]}}</span>
				</td></tr>
	    	</li>
	    %end
	    <li class="list-group-item list-group-item-info">
			<tr>
			    <td>
			    	<label>车头照片:&nbsp</label>
			    	<a href="/static/{{detail[1][-3]}}" class="thumbnail">
	      				<img src="/static/{{detail[1][-3]}}" alt="车头">
	    			</a>
			    </td>
			</tr>
			<tr>
			    <td>
			    	<label>车尾照片:&nbsp</label>
			    	<a href="/static/{{detail[1][-2]}}" class="thumbnail">
	      				<img src="/static/{{detail[1][-2]}}" alt="车尾">
	    			</a>
			    </td>
			<tr>
		</li>
  	</ul>
  </div>
  <div class="panel-heading panel-warning">
    <h4 class="panel-title">历史信息</h4>
  </div>
  <div class="panel-body">
  	%for rec in history_recs[1:]:
  		<ul class="list-group">
		    %for i in xrange(0, len(history_recs[0])):
		    	%if (i==3) and isblack:
		    	<li class="list-group-item list-group-item-danger">
		    	%elif (i==0) and rec[-1]=="未处理":
		    	<li class="list-group-item list-group-item-danger">
		    	%else:
		    	<li class="list-group-item list-group-item-info">
		    	%end
		    		<tr><td>
						<label>{{history_recs[0][i]}}:&nbsp</label>
	    		    	<span>{{rec[i]}}</span>
					</td></tr>
		    	</li>
		    %end
		    <li class="list-group-item list-group-item-info">
				<tr>
				    <td>
				    	<label>车头照片:&nbsp</label>
				    	<a href="/static/{{rec[-3]}}" class="thumbnail">
		      				<img src="/static/{{rec[-3]}}" alt="车头">
		    			</a>
				    </td>
				</tr>
				<tr>
				    <td>
				    	<label>车尾照片:&nbsp</label>
				    	<a href="/static/{{rec[-2]}}" class="thumbnail">
		      				<img src="/static/{{rec[-2]}}" alt="车尾">
		    			</a>
				    </td>
				<tr>
			</li>
  		</ul>
  	%end
  </div>
</div>


%include ('./view/bsfiles/view/html_footer.tpl')