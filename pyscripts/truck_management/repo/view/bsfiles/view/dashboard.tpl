%include ('./view/bsfiles/view/html_hdr.tpl')

%include ('./view/bsfiles/view/navbar.tpl')

    <div class="container-fluid">
      <div class="row">
        %include ('./view/bsfiles/view/nav_sidebar.tpl')
        <div class="col-xs-8 col-xs-offset-4 col-sm-8 col-sm-offset-4 
                    col-md-10 col-md-offset-2 col-lg-10 col-lg-offset-2 main">
          <h2 class="page-header">数据概要</h2>

          <div class="row placeholders">
            <div class="col-xs-3 col-sm-3 placeholder">
              <!--img data-src="holder.js/200x200/auto/sky" class="img-responsive" alt="Generic placeholder thumbnail"-->
              <h4>今日超限违章</h4>
              <button class="btn btn-primary" type="button">
                违章个数 <span class="badge">0</span>
              </button>
            </div>
            <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 placeholder">
              <!--img data-src="holder.js/200x200/auto/vine" class="img-responsive" alt="Generic placeholder thumbnail"-->
              <h4>本周超限违章</h4>
              <button class="btn btn-primary" type="button">
                违章个数 <span class="badge">0</span>
              </button>
            </div>
            <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 placeholder">
              <!--img data-src="holder.js/200x200/auto/sky" class="img-responsive" alt="Generic placeholder thumbnail"-->
              <h4>本月超限违章</h4>
              <button class="btn btn-primary" type="button">
                违章个数 <span class="badge">0</span>
              </button>
            </div>
            <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 placeholder">
              <!--img data-src="holder.js/200x200/auto/vine" class="img-responsive" alt="Generic placeholder thumbnail"-->
              <h4>黑名单</h4>
              <button class="btn btn-primary" type="button">
                黑名单个数 <span class="badge">0</span>
              </button>
            </div>
          </div>

          %if query_results:
            %include (query_results)
          %end
          <!--div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1,001</td>
                  <td>Lorem</td>
                  <td>ipsum</td>
                  <td>dolor</td>
                  <td>sit</td>
                </tr>
              </tbody>
            </table>
          </div-->
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/view/bsfiles/js/jquery.min.js"></script>
    <script src="/static/view/bsfiles/js/bootstrap.min.js"></script>

%include ('./view/bsfiles/view/html_footer.tpl')
