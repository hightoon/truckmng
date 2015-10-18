%include ('./view/bsfiles/view/html_hdr.tpl')

%include ('./view/bsfiles/view/navbar.tpl')

    <div class="container-fluid">
      <div class="row">
        %include ('./view/bsfiles/view/nav_sidebar.tpl')
        <div class="col-xs-8 col-xs-offset-4 col-sm-8 col-sm-offset-4 
                    col-md-10 col-md-offset-2 col-lg-10 col-lg-offset-2 main">
          <h2 class="page-header">数据概要</h2>

          <!--div class="row placeholders placeholder">
            <div class="col-xs-3 col-sm-3 placeholder">
              <h4>今日超限违章</h4>
              <button class="btn btn-primary" type="button">
                今日违章个数 <span class="badge">0</span>
              </button>
            </div>
            <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 placeholder">
              <h4>本周超限违章</h4>
              <button class="btn btn-primary" type="button">
                违章个数 <span class="badge">0</span>
              </button>
            </div>
            <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 placeholder">
              <h4>本月超限违章</h4>
              <button class="btn btn-primary" type="button">
                违章个数 <span class="badge">0</span>
              </button>
            </div>
            <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 placeholder">
              <h4>黑名单</h4>
              <button class="btn btn-primary" type="button">
                黑名单个数 <span class="badge">0</span>
              </button>
            </div>
          </div-->

          %if query_results:
            %include (query_results)
          %end
          <div class="panel panel-danger">
          <!-- Default panel contents -->
            <div class="panel-heading">站点今日各时段违章</div>
              <div class="panel-body">
                <div id="line-stat"></div>
              </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!--script src="http://code.jquery.com/jquery-1.9.0.js"></script>
    <script scr="/static/view/bsfiles/js/raphael.js"></script>
    <script src="/static/view/bsfiles/js/morris.js-0.5.1/morris.js"></script-->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
    <script src="http://code.jquery.com/jquery-1.8.2.min.js"></script>
    <script src="http://cdn.oesmith.co.uk/morris-0.4.1.min.js"></script>
    <script src="/static/view/bsfiles/js/JSON-js-master/json2.js"></script>
    <script type="text/javascript">
      var numofsite = {{numofsite}};
      var sites = ["{{sites}}"];
      var data = JSON.parse("{{stat}}");
      var statdata = [];
      for (var i = 0; i < 24; i++) {
        d = {};
        d['h'] = String(i)+':00';
        for (var j = 0; j < numofsite; j++) {
          d[sites[j]] = data[numofsite*i+j];
        }
        statdata.push(d);
      }
      Morris.Line({element: 'line-stat',
        parseTime: false,
        data: statdata,
        xkey: 'h',
        ykeys: sites,
        labels: sites});
    </script>
    <script src="/static/view/bsfiles/js/jquery.min.js"></script>
    <script src="/static/view/bsfiles/js/bootstrap.min.js"></script>

%include ('./view/bsfiles/view/html_footer.tpl')
