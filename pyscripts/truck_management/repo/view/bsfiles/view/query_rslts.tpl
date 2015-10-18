<div class="panel panel-danger">
  <!-- Default panel contents -->
  <div class="panel-heading">站点超限统计－{{period}}</div>
  <div class="panel-body"></div>
  <!-- Table -->
  <h4 style="color:red;">站点超限总数</h4>
  <table class="table">
	<thead>
		<tr>
		  <th>序号</th>
		  <th>站点</th>
		  <th>总超限车次</th>
		</tr>
	</thead>
	<tbody>
		%for i in xrange(numofsite):
			<td>{{i+1}}</td>
			<td>{{sites[i]}}</td>
			<td>{{sum([res[sites[i]] for res in stat])}}</td>
		%end
	</tbody>
  </table>
  <h4 style="color:red;">站点超限分时段统计</h4>
  %for i in xrange(numofsite):
  	<span style="color: blue">{{sites[i]}}</span>
  	<table class="table">
	<thead>
		<tr>
		  <th>序号</th>
		  <th>时段</th>
		  <th>超限车次</th>
		</tr>
	</thead>
	<tbody>
		%for h in xrange(24):
		  <tr>
			<td>{{h+1}}</td>
			<td>{{h}}:00-{{h+1}}:00</td>
			<td>{{stat[h][sites[i]]}}</td>
	      </tr>
		%end
	</tbody>
  </table>
  %end
  <h4 style="color:red;">站点分时段超限率统计</h4>
  <table class="table">
	<thead>
		<tr>
		  <th>序号</th>
		  <th>站点</th>
		  <th>未超限(0%)</th>
		  <th>超限0%~20%</th>
		  <th>超限20%~50%</th>
		  <th>超限50%~100%</th>
		  <th>超限100%以上</th>
		</tr>
	</thead>
	<tbody>
		%for i in xrange(numofsite):
		  <tr>
			<td>{{i+1}}</td>
			<td>{{sites[i]}}</td>
			%for j in xrange(5):
				<td>{{percent[sites[i]][j]}}</td>
			%end
	      </tr>
		%end
	</tbody>
  </table>
</div>