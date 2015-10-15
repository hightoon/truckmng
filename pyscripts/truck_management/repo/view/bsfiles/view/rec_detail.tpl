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
</div>
%include ('./view/bsfiles/view/html_footer.tpl')