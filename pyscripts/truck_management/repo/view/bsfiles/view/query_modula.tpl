<div class="modal fade" tabindex="-1" role="document" id="rec-modula">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <h3 class="sub-header">纪录详情</h3>
	  <table class="table table-striped table-responsive">  
	    <thead>
	        <tr>
	      	  %for col in details[0]:
	      	    <th>{{col}}</th>
	      	  %end
	      	</tr>
	    </thead>
	    <tbody>
	      	<tr>
	      	  %for col in detail:
	      	    <td>{{col}}</td>
	      	  %end
	      	</tr>
	    </tbody>
	   </table>
	    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
		  <!-- Indicators -->
		  <ol class="carousel-indicators">
		    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
		    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
		  </ol>

		  <!-- Wrapper for slides -->
		  <h4>车辆照片</h4>
		  <div class="carousel-inner" role="listbox">
		    <div class="item active">
		      <img src="http://d6.yihaodianimg.com/N03/M09/BD/64/CgQCtVNRDUKAFbKXAAFSdWsrqx406300.jpg" alt="车头照片">
		      <div class="carousel-caption">
		        车头照片
		      </div>
		    </div>
		    <div class="item">
		      <img src="http://d6.yihaodianimg.com/N03/M09/BD/64/CgQCtVNRDUKAFbKXAAFSdWsrqx406300.jpg" alt="车尾照片">
		      <div class="carousel-caption">
		        车尾照片
		      </div>
		    </div>
		  </div>

		  <!-- Controls -->
		  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
		    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
		    <span class="sr-only">Previous</span>
		  </a>
		  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
		    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
		    <span class="sr-only">Next</span>
		  </a>
		</div>
    </div>
  </div>
</div>