        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><em><a href="/query">数据查询</a></em>
                <!--a href="#">数据查询 <span class="sr-only">(current)</span></a-->
            </li>
            <li><a href="#">车辆数据</a></li>
            <li><a href="#">待处理数据</a></li>
            <li><a href="#">处理登记数据</a></li>
          </ul>
          <ul class="nav nav-sidebar">
            <li>
              <span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><em><a href="/index">数据统计</a></em>
            </li>
          </ul>
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><em><a href="/proceed">超限纪录审核</a></em>
            </li>
            %if "超限处理" in privs:
              <li><a href="/proceed">超限处理</a></li>
            %end
            %if "处理审核" in privs:
              <li><a href="">处理审核</a></li>
            %end
          </ul>
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><em><a href="">超限处理登记</a></em></li>
            %if "超限处理登记" in privs:
              <li><a href="">添加纪录</a></li>
              <li><a href="">删除纪录</a></li>
            %end
            %if "登记审核" in privs:
              <li><a href="">登记审核</a></li>
            %end
          </ul>
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><em><a href="">黑名单管理</a></em></li>
            <li><a href="">查询</a></li>
            %if "黑名单增删" in privs:
              <li><a href="">添加删除</a></li>
            %end
            %if "黑名单审核" in privs:
              <li><a href="">审核</a></li>
            %end
          </ul>
          <ul class="nav nav-sidebar">
            %if "用户增删" in privs:
              <li><span class="glyphicon glyphicon-hand-right" aria-hidden="false"></span><em><a href="">用户管理</a></em></li>
              <li><a href="/account_mngn">添加删除</a></li>
            %end
          </ul>
        </div>