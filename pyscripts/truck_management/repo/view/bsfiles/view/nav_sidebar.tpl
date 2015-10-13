        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><a href="/query">数据查询</a>
                <!--a href="#">数据查询 <span class="sr-only">(current)</span></a-->
            </li>
            <!--li><a href="#">车辆数据</a></li>
            <li><a href="#">待处理数据</a></li>
            <li><a href="#">处理登记数据</a></li-->
          </ul>
          <ul class="nav nav-sidebar">
            <li>
              <span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span><a href="/index">数据统计</a>
            </li>
          </ul>
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>超限纪录审核
            </li>
            %if "超限处理" in privs:
              <li><a href="/proceed">超限处理</a></li>
            %end
            %if "处理审核" in privs:
              <li><a href="/proceed_approval">处理审核</a></li>
            %end
          </ul>
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>超限处理登记</li>
            %if "超限处理登记" in privs:
              <li><a href="/register">增删纪录</a></li>
            %end
            %if "超限处理登记审核" in privs:
              <li><a href="/reg_approval">登记审核</a></li>
            %end
          </ul>
          <ul class="nav nav-sidebar">
            <li><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>黑名单管理</li>
            <li><a href="/blacklist_query">查询</a></li>
            %if "黑名单增删" in privs:
              <li><a href="/blacklist_mng">添加删除</a></li>
            %end
            %if "黑名单审核" in privs:
              <li><a href="/blacklist_approval">审核</a></li>
            %end
          </ul>
          <ul class="nav nav-sidebar">
            %if "用户增删" in privs:
              <li><span class="glyphicon glyphicon-hand-right" aria-hidden="false"></span><a href="/account_mngn">用户管理</a></li>
              <!--li><a href="/account_mngn">添加删除</a></li-->
            %end
          </ul>
        </div>