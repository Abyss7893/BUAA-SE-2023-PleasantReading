<!-- 网页头部顶侧，包含logo、登录&&注册、搜索栏等 -->
<template>
  <div class="proeffect">
    <ElDialog v-model="showLogin" style="background-color: transparent; width: 800px;">
      <newLogin class="mycardlogin" v-if="showLogin" style="z-index: 1000; background-color: transparent;"
        @submit="showLogin = false" ref="login"></newLogin>
    </ElDialog>
  </div>
  <link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.0.0/animate.min.css" />
  <div class="placeholder" style="height: 64px;" v-if="holdplace"></div>
  <div class="head-top" :class="navishow ? 'slide-down' : ''" :id="navishow ? 'fixheight' : ''">
    <!-- <check-login/> -->
    <div v-if="navishow">
      <a class="logoa hvr-buzz-out" href="/"><img class="logo" src="~assets/logo-yixinyuedu.png" alt="" /></a>
    </div>
    <div class="left-navi" v-if="navishow">
      <li navi-id="1">
        <a href="#">首页</a>
      </li>
      <li navi-id="2">
        <a href="#">全部作品</a>
      </li>
      <li navi-id="3">
        <a href="#" class="hover-me">作品排行</a>
        <div class="hover-card">
          <div class="left">
            <div class="title">推荐书目</div>
            <div class="book-list">
             <p class="book-list-item" @click="showmycard(0)">{{ bookdata[0].title }}</p>
             <p class="book-list-item" @click="showmycard(1)">{{ bookdata[1].title }}</p>
             <p class="book-list-item" @click="showmycard(2)">{{ bookdata[2].title }}</p>
             <p class="book-list-item" @click="showmycard(3)">{{ bookdata[3].title }}</p>
             <p class="book-list-item" @click="showmycard(4)">{{ bookdata[4].title }}</p>  
            </div>
          </div>
          <div class="right">
            
            <div class="card" id="card">
              
                <div class="photo">
                      <img :src="showdata.avg" alt="">
                </div>
                <h1>{{showdata.title}}</h1>
                <h2>{{showdata.author}}</h2>
                <p>{{showdata.profile}}</p>
                <a style="height: 40px; margin-bottom: 10px;" href="#">toda</a>
                <div class="close-icon" @click="closeIcon"><svg class="closeicon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M851.416 217.84l-45.256-45.248L512 466.744l-294.152-294.16-45.256 45.256L466.744 512l-294.152 294.16 45.248 45.256L512 557.256l294.16 294.16 45.256-45.256L557.256 512z" fill="#272536"></path></svg></div>
              </div>
          </div>
        </div>
      </li>
    </div>
    <div class="dropdown">
      <div class="search">
        <div class="shell">
          <input type="text" placeholder="Search" v-model="keywords" @focusin="drop" @focusout="hide">
          <svg @mousedown="clearwords" v-show="keywords !== ''" class="clear" width="16" height="16" viewBox="0 0 16 16"
            fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd"
              d="M8 14.75C11.7279 14.75 14.75 11.7279 14.75 8C14.75 4.27208 11.7279 1.25 8 1.25C4.27208 1.25 1.25 4.27208 1.25 8C1.25 11.7279 4.27208 14.75 8 14.75ZM9.64999 5.64303C9.84525 5.44777 10.1618 5.44777 10.3571 5.64303C10.5524 5.83829 10.5524 6.15487 10.3571 6.35014L8.70718 8.00005L10.3571 9.64997C10.5524 9.84523 10.5524 10.1618 10.3571 10.3571C10.1618 10.5523 9.84525 10.5523 9.64999 10.3571L8.00007 8.70716L6.35016 10.3571C6.15489 10.5523 5.83831 10.5523 5.64305 10.3571C5.44779 10.1618 5.44779 9.84523 5.64305 9.64997L7.29296 8.00005L5.64305 6.35014C5.44779 6.15487 5.44779 5.83829 5.64305 5.64303C5.83831 5.44777 6.15489 5.44777 6.35016 5.64303L8.00007 7.29294L9.64999 5.64303Z"
              fill="#fff"></path>
          </svg>
          <div class="proshake">
            <a @click="searchBooks">
              <i class="fa fa-hand-o-right"></i>
              <i class="fa fa-search"></i>
            </a>
          </div>
        </div>
      </div>
      <div class="dropdown-content" ref="hidden">
        <div class="first-want">大家都想看</div>
        <div class="want" v-for="(searchHot, idx) in searchHots" :key="idx" @click="searchBooks(searchHot)">{{ searchHot
        }}</div>
      </div>
    </div>
    <div class="right-navi" :id="navishow ? 'fixmargin' : ''">
      <div class="login-register">
        <template v-if="!isLogin">
          <div class="avatar">
            <el-popover trigger="hover" :show-arrow=false transition="el-zoom-in-top" width="480">
              <div class="logininfo">登录后你可以</div>
              <div class="login-pri">
                <li><svg t="1685433487956" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="2670" width="24" height="24">
                    <path
                      d="M880 184H712v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H384v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H144c-17.7 0-32 14.3-32 32v664c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V216c0-17.7-14.3-32-32-32z m-40 656H184V256h128v48c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8v-48h256v48c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8v-48h128v584z"
                      p-id="2671" fill="#ed4259"></path>
                    <path
                      d="M639.5 414h-45c-3 0-5.8 1.7-7.1 4.4L514 563.8h-2.8l-73.4-145.4c-1.4-2.7-4.1-4.4-7.1-4.4h-46c-1.3 0-2.7 0.3-3.8 1-3.9 2.1-5.3 7-3.2 10.9l89.3 164h-48.6c-4.4 0-8 3.6-8 8v21.3c0 4.4 3.6 8 8 8h65.1v33.7h-65.1c-4.4 0-8 3.6-8 8v21.3c0 4.4 3.6 8 8 8h65.1V752c0 4.4 3.6 8 8 8h41.3c4.4 0 8-3.6 8-8v-53.8h65.4c4.4 0 8-3.6 8-8v-21.3c0-4.4-3.6-8-8-8h-65.4v-33.7h65.4c4.4 0 8-3.6 8-8v-21.3c0-4.4-3.6-8-8-8h-49.1l89.3-164.1c0.6-1.2 1-2.5 1-3.8 0.1-4.4-3.4-8-7.9-8z"
                      p-id="2672" fill="#ed4259"></path>
                  </svg>免费阅读大量书籍</li>
                <li><svg t="1685433539490" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="3810" width="24" height="24">
                    <path d="M192 320l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3811"></path>
                    <path d="M320 320l448 0 0 64-448 0 0-64Z" fill="#ed4259" p-id="3812"></path>
                    <path d="M192 512l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3813"></path>
                    <path d="M320 512l448 0 0 64-448 0 0-64Z" fill="#ed4259" p-id="3814"></path>
                    <path d="M192 704l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3815"></path>
                    <path d="M320 704l448 0 0 64-448 0 0-64Z" fill="#ed4259" p-id="3816"></path>
                    <path d="M320 64l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3817"></path>
                    <path
                      d="M832 75.776l0 65.984C872.64 161.152 896 200.704 896 256l0 576c0 66.688-45.312 128-128 128L192 960c-61.312 0-128-64-128-128L64 256c0-46.592 25.6-87.872 64-110.272L128 75.776C53.568 102.208 0 172.544 0 256l0 576c0 106.048 85.952 192 192 192l576 0c106.048 0 192-85.952 192-192L960 256C960 172.544 906.432 102.208 832 75.776z"
                      fill="#ed4259" p-id="3818"></path>
                    <path d="M576 64l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3819"></path>
                    <path d="M192 0l64 0 0 192-64 0 0-192Z" fill="#ed4259" p-id="3820"></path>
                    <path d="M448 0l64 0 0 192-64 0 0-192Z" fill="#ed4259" p-id="3821"></path>
                    <path d="M704 0l64 0 0 192-64 0 0-192Z" fill="#ed4259" p-id="3822"></path>
                  </svg>发表评论/记录笔记</li>
                <li><svg t="1685433591589" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="4934" width="24" height="24">
                    <path
                      d="M282.766507 610.432L100.494507 401.92 370.361173 340.48 512.014507 102.656l141.610666 237.909333 269.824 61.397334-182.272 208.512 27.306667 300.757333a42.666667 42.666667 0 0 0 84.992-7.722667l-24.021333-264.405333 174.634666-199.722667c38.144-43.648 19.2-102.229333-37.418666-115.114666l-258.474667-58.794667-135.68-228.010667c-29.738667-49.877333-91.306667-49.92-121.045333 0L315.74784 265.429333 57.273173 324.224C0.953173 337.066667-18.33216 395.648 19.854507 439.338667l174.634666 199.722666-24.021333 264.405334c-5.248 57.770667 44.544 94.037333 97.877333 71.125333l260.48-111.786667a42.666667 42.666667 0 1 0-33.706666-78.378666L257.721173 886.314667l25.045334-275.882667z"
                      fill="#ed4259" p-id="4935"></path>
                  </svg>收藏喜欢的图书</li>
                <li><svg t="1685433451224" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="1480" width="24" height="24">
                    <path
                      d="M748.739048 352.865524c-32.743619-40.496762-29.915429 86.893714-68.169143 67.462095-38.253714-19.431619-27.087238-285.891048-259.169524-354.230857-92.769524-27.306667 36.766476 218.35581-104.374857 331.751619-141.165714 113.371429-340.845714 359.765333 113.615238 562.151619 0 0-235.398095-269.409524 68.144762-427.227429 69.632-36.205714-22.723048 89.941333 90.89219 179.882667 113.615238 89.965714 0 247.344762 0 247.344762s516.291048-165.059048 159.061334-607.134476z"
                      p-id="1481" fill="#ed4259"></path>
                  </svg>热门书籍看不停</li>
              </div>
              <el-button class="login-button" type="primary" color="#f33f3f" @click="showLoginblock">立即登录</el-button>
              <div class="register"><span>首次使用?<a @click="showRegister">点我注册</a></span></div>
              <template #reference>
                <ElAvatar class="login-avatar" size="large"><span @click="showLoginblock">登录</span></ElAvatar>
              </template>
            </el-popover>
          </div>
        </template>
        <template v-else>
          <div class="avatar" @mouseleave="popleave">
            <!-- <ElDropdown trigger="click"> -->
            <div class="edavatar" ref="edavatar" @mouseenter="popover">
              <router-link to="/user/info">
                <ElAvatar :src="avatar" size="large"></ElAvatar>
              </router-link>
            </div>
            <div :style="{ opacity: popShow }" class="popuserinfo hidden" ref="popuserinfo">
              <popUserInfo />
            </div>
          </div>
        </template>
      </div>
      <ul v-if="navishow">
        <li navi-id="4" >
          <svg class="icon" style="vertical-align: middle; overflow: hidden;" viewBox="0 0 1081 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path stroke-width="4" d="M356.577333 1023.999988a25.9364 25.9364 0 0 1-19.035889-8.328202L148.574547 812.059152a25.960194 25.960194 0 0 1 38.071779-35.299677l175.070697 188.705153 250.024513-139.616353a26.959579 26.959579 0 0 0 13.527379-19.190556l57.869104-346.215242a25.948297 25.948297 0 0 1 51.158953 8.554253l-57.881001 346.215242a78.523045 78.523045 0 0 1-39.428087 55.917925L369.224302 1020.716297a25.900707 25.900707 0 0 1-12.646969 3.283691z" fill="#0E4F53"></path><path stroke-width="4" d="M1002.500759 404.786295a25.9364 25.9364 0 0 1-19.476094-43.044906c67.910536-77.416583 60.177206-195.66515-17.239378-263.599481S770.096342 37.9766 702.197704 115.393183a25.942348 25.942348 0 0 1-39.011677-34.205114c86.756067-98.867652 237.85344-108.837699 336.804374-22.034042s108.813904 237.877235 22.022145 336.804374a25.84122 25.84122 0 0 1-19.511787 8.827894z" fill="#9B4537"></path><path stroke-width="4" d="M389.354756 824.658532c-1.189743 0-2.379486 0-3.640614-0.083282L79.307704 810.667153a25.960194 25.960194 0 0 1-24.365939-21.415376L1.260557 487.294979a78.523045 78.523045 0 0 1 18.38153-65.959358L297.090178 105.078111c103.757496-118.236669 284.419985-130.050818 402.704244-26.293323s130.098408 284.419985 26.35281 402.692347L448.675347 797.734645a78.523045 78.523045 0 0 1-59.320591 26.923887z m-1.29682-51.920389a27.364091 27.364091 0 0 0 21.617632-9.220509l277.44809-316.245613C772.011829 350.498317 762.363012 202.684634 665.577411 117.784567s-244.575489-75.227456-329.487454 21.58194L58.701353 455.576428a26.983373 26.983373 0 0 0-6.305638 22.605118L102.448207 759.758046z" fill="#0E4F53"></path><path stroke-width="4" d="M525.16393 376.291947a98.582113 98.582113 0 1 1 74.23997-33.57455 97.975344 97.975344 0 0 1-67.672588 33.312807c-2.201025 0.178461-4.390152 0.261743-6.567382 0.261743z m0.154667-145.315222A46.685519 46.685519 0 1 0 560.380326 308.452796a46.673622 46.673622 0 0 0-35.061729-77.476071zM962.834724 552.945003a98.6416 98.6416 0 1 1 52.420081-15.240609 98.582113 98.582113 0 0 1-52.420081 15.240609z m-0.309333-145.315222a46.947263 46.947263 0 1 0 10.410252 1.189743 46.399981 46.399981 0 0 0-10.410252-1.189743z" fill="#0E4F53"></path><path stroke-width="4" d="M133.060297 617.797899a25.960194 25.960194 0 0 1-25.579476-21.867478l-17.608198-110.348672a25.995887 25.995887 0 0 1 5.544202-20.511171l71.289407-87.065401a25.948297 25.948297 0 0 1 40.15383 32.872602l-63.913 78.047148 15.764096 98.879549a25.9364 25.9364 0 0 1-21.53435 29.743577 25.460502 25.460502 0 0 1-4.116511 0.249846z" fill="#CDC1AD"></path></svg>
          <a href="#">我的书签</a>
        </li>
        <li navi-id="5">
          <svg class="icon" style="vertical-align: middle; overflow: hidden;" viewBox="0 0 1097 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M998.58390632 852.14701166H126.84569332A41.51236 41.51236 0 0 0 85.33333332 893.65937166v62.26854a41.51236 41.51236 0 0 0 41.51236 41.51236h871.738213a41.51236 41.51236 0 0 0 41.51236-41.51236v-62.26854a41.51236 41.51236 0 0 0-41.51236-41.51236z m-29.293426 83.014048h-813.172704a8.537246 8.537246 0 0 1-8.537246-8.537246v-3.681687a8.537246 8.537246 0 0 1 8.537246-8.537247h813.172704a8.537246 8.537246 0 0 1 8.537246 8.537247v3.681687a8.537246 8.537246 0 0 1-8.537246 8.537246zM126.84569332 810.63465166h124.537079a41.51236 41.51236 0 0 0 41.51236-41.51236V229.47228566a41.51236 41.51236 0 0 0-41.51236-41.51236H126.84569332A41.51236 41.51236 0 0 0 85.33333332 229.47228566v539.650006a41.51236 41.51236 0 0 0 41.51236 41.51236zM156.72605532 246.49342066h64.883071a12.805869 12.805869 0 0 1 12.805869 12.805869v479.995998a12.805869 12.805869 0 0 1-12.805869 12.80587H156.72605532a12.805869 12.805869 0 0 1-12.80587-12.80587V259.29928966a12.805869 12.805869 0 0 1 12.80587-12.805869z m239.939305 564.141231h124.53708a41.51236 41.51236 0 0 0 41.51236-41.51236V278.62548066l291.653674 510.335237 0.266789 0.480221a41.619075 41.619075 0 0 0 56.826045 15.527116l107.932136-62.962191A42.600859 42.600859 0 0 0 1034.18422332 684.02729066L727.73976932 147.49337866l-0.266789-0.48022a41.619075 41.619075 0 0 0-56.826045-15.527116l-107.932135 62.962191V84.17902666A41.51236 41.51236 0 0 0 521.20244032 42.66666666h-124.53708a41.51236 41.51236 0 0 0-41.51236 41.51236v684.943265a41.51236 41.51236 0 0 0 41.51236 41.51236z m296.295802-597.938055a3.735045 3.735045 0 0 1 5.122348 1.376631l259.841761 454.608363a12.805869 12.805869 0 0 1-4.663471 17.415982l-56.271124 32.825712a12.805869 12.805869 0 0 1-17.544041-4.663471L624.11894332 267.59109066a12.805869 12.805869 0 0 1 4.663471-17.415983zM426.49236432 101.20016166h64.883072a12.805869 12.805869 0 0 1 12.805869 12.805869v625.289257a12.805869 12.805869 0 0 1-12.805869 12.80587h-64.883072a12.805869 12.805869 0 0 1-12.805869-12.80587V114.00603066a12.805869 12.805869 0 0 1 12.805869-12.805869z m0 0"></path></svg>
          <a href="#">我的书架</a>
        </li>
        <li navi-id="6">
          <svg style="width: 25px;margin: 0 0 -30px 34px;" viewBox="0 0 1024 1430" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M192 309.333333H21.333333a21.333333 21.333333 0 0 1-21.333333-21.333333 21.333333 21.333333 0 0 1 21.333333-21.333333h170.666667a21.333333 21.333333 0 0 1 21.333333 21.333333 21.333333 21.333333 0 0 1-21.333333 21.333333zM192 423.04H21.333333a21.333333 21.333333 0 0 1-21.333333-21.333333 21.333333 21.333333 0 0 1 21.333333-21.333334h170.666667a21.333333 21.333333 0 0 1 21.333333 21.333334 21.333333 21.333333 0 0 1-21.333333 21.333333zM192 536.96H21.333333a21.333333 21.333333 0 0 1-21.333333-21.333333 21.333333 21.333333 0 0 1 21.333333-21.333334h170.666667a21.333333 21.333333 0 0 1 21.333333 21.333334 21.333333 21.333333 0 0 1-21.333333 21.333333zM192 650.666667H21.333333a21.333333 21.333333 0 0 1-21.333333-21.333334 21.333333 21.333333 0 0 1 21.333333-21.333333h170.666667a21.333333 21.333333 0 0 1 21.333333 21.333333 21.333333 21.333333 0 0 1-21.333333 21.333334zM917.333333 650.666667h-170.666666a106.666667 106.666667 0 0 1-106.666667-106.666667v-85.333333a106.666667 106.666667 0 0 1 106.666667-106.666667h170.666666a106.666667 106.666667 0 0 1 106.666667 106.666667v85.333333a106.666667 106.666667 0 0 1-106.666667 106.666667z m-170.666666-256a64 64 0 0 0-64 64v85.333333a64 64 0 0 0 64 64h170.666666a64 64 0 0 0 64-64v-85.333333a64 64 0 0 0-64-64z"></path><path d="M832 1024H192a106.666667 106.666667 0 0 1-106.666667-106.666667V106.666667a106.666667 106.666667 0 0 1 106.666667-106.666667h640a106.666667 106.666667 0 0 1 106.666667 106.666667v288h-192a64 64 0 0 0-64 64v85.333333a64 64 0 0 0 64 64h192V917.333333a106.666667 106.666667 0 0 1-106.666667 106.666667zM192 42.666667a64 64 0 0 0-64 64v810.666666a64 64 0 0 0 64 64h640a64 64 0 0 0 64-64V650.666667h-149.333333a106.666667 106.666667 0 0 1-106.666667-106.666667v-85.333333a106.666667 106.666667 0 0 1 106.666667-106.666667h149.333333V106.666667a64 64 0 0 0-64-64z"></path></svg>
          <a href="#">我的笔记</a>
        </li>
      </ul>
    </div>
    <div v-if="navishow" style="width: 100px;height: 10px;"></div>
  </div>
</template>


<script>
import "css/head/headtop.css";
import newLogin from "@/components/page/login/newLogin.vue";
import { mapGetters } from "vuex";
import {
  ElAvatar, ElDialog,
  // ElDropdown,
  // ElDropdownMenu,
  // ElDropdownItem,
} from "element-plus";
import popUserInfo from "./popUserInfo.vue"
export default {
  name: "Head_Top",
  components: {
    ElAvatar,
    popUserInfo,
    newLogin,
    ElDialog
  },
  props: {
    navishow: {
      type: Boolean,
      default: true
    },
    holdplace: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      showdata:{avg:"1"},
      bookdata:[{
        avg:'	http://154.8.183.51/media/BookImg/default.jpg',
        title:'重生之我在北航卖西瓜',
        author:'奈奈酱想摸鱼c',
        profile:'林恩挑战魔君失败后，意外获得了回溯时间的能力，当他再次睁眼，已经成了北航旁边一个...',
      },
      {
        avg: 'http://154.8.183.51/media/BookImg/abCZwBoz.jpg',
        title: '英灵时代，十连保底',
        author: '苹果咖啡味',
        profile: '我叫白榆，是一个超能力者。 超能力名为保底法则。 买饮料十次，最后一次必然是...',
      },
      {
        avg: '	http://154.8.183.51/media/BookImg/teeZ85vW.jpg',
        title: '综武：偷看我的日记',
        author: '路人.v1',
        profile: '人在综武，每天写日记就能变强。 定个小目标，没成天下第一之前好好苟起来。 只是...',
      },
      {
        avg: 'http://154.8.183.51/media/BookImg/ELOymcKb.jpg',
        title: '综武：龙之初，性本善',
        author: '扫墓上坟',
        profile: '苍龙大陆； 十八岁的林魏一朝觉醒前世记忆，原本计划着继承父亲家业，苟且度日。没曾想...',
      },
      {
        avg: 'http://154.8.183.51/media/BookImg/XjymiETu.jpg',
        title: '被迫当反派的我义字为先',
        author: '夜影.cs',
        profile: '我行我的路，你笑你的痴。利字腰间挂，情义两肩挑。侠情柔骨何处觅，自上心乡寻宝刀。',
      },
    ],
      searchHots: ["青春北航男童不会梦到清华女学长", "重生之我在北航卖西瓜", "飘飘何所似", "红楼梦", "杨过"],
      clearExit: false,
      keywords: "",
      showLogin: false,
      popShow: 0,
      throttling1: false,
    }
  },
  
  computed: {
    avatar() {
      return this.$store.state.userAvatar;
    },
    isLogin() {
      return this.$store.state.isLogin;
    },
    clearShow() {
      return this.clearExit
    },
    ...mapGetters(['loginshow']),
  },
  watch: {
    loginshow() {
      this.showLogin = true
    }
  },
  mounted() {
    this.keywords = this.$route.query.keywords ? this.$route.query.keywords : ""
  },
  methods: {
    onCloseDialog(value) {
      // 接收到子组件传递过来的布尔值，赋值给 showLogin 属性
      this.showLogin = value;
    },
    drop() {
      this.$refs.hidden.style.maxHeight = '500px';
      this.$refs.hidden.style.paddingBottom = '10px'
    },
    hide() {
      this.$refs.hidden.style.maxHeight = '0';
      this.$refs.hidden.style.paddingBottom = '0'
    },
    closeIcon(){
      const mycard = document.getElementById('card');
      mycard.classList.toggle('show-card')

    },
    showmycard(num){
      const mycard=document.getElementById('card');
      console.log(this.showdata)
      if(this.showdata==this.bookdata[num]){
        mycard.classList.toggle('show-card')
      }
      this.showdata=this.bookdata[num]
    },
    searchBooks(keywords) {
      if (typeof (keywords) != "string")
        keywords = this.keywords
      if (keywords === '')
        return
      this.$router.push({ path: '/search', query: { "keywords": keywords, page: 1 } })
    },
    clearwords() {
      this.keywords = ""
    }, showLogina() {
      this
    },
    popover() {
      if (!this.throttling2) {
        this.throttling2 = true
        this.$refs.popuserinfo.classList.remove("hidden")
        this.popShow = "1"
        this.$refs.edavatar.classList.add("large")
        // this.$refs.edavatar.classList.add("large")
      }
    },
    popleave() {
      this.$refs.edavatar.classList.remove("large")
      this.$refs.popuserinfo.classList.add("hidden")
      this.popShow = "0"
      setTimeout(() => {
        this.throttling2 = false
      }, 400);
    },
    showLoginblock() {
      this.showLogin = true
      setTimeout(() => {
        if (this.$refs.login.showStatus())
          this.$refs.login.changeForm()
      }, 200)
    },
    showRegister() {
      this.showLogin = true
      setTimeout(() => {
        if (!this.$refs.login.showStatus())
          this.$refs.login.changeForm()
      }, 200)
    },
  },

}
</script>
<style scoped>
#fixheight {
  height: 64px;
}

#fixheight .dropdown {
  margin: 0;
}

.dropdown {
  margin: 0 36px 0 236px;
}

.slide-down {
  display: flex;
  justify-content: space-between;
  position: fixed;
  top: 0;
  width: 100%;
  min-width: 1200px;
  z-index: 200;
  background-color: #f5f5f5;
  animation: headerSlideDown .3s linear forwards;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .08);
}

@keyframes headerSlideDown {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

.mycardlogin {
  z-index: 1000;
  background-color: transparent;

}

.hidden {
  visibility: hidden;
  z-index: -100;
}

.mask {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  width: 100%;
  height: 100%;
  background-color: rgba(254, 253, 253, 0.5);
}

.shell {
  position: relative;
  width: 500px;
  padding: 16px;
  background-color: #ff7575;
  border-radius: 20px;
  box-shadow: 0 10px 50px #ff7575, 0 0 0 20px #fff;
}

.shell {
  position: relative;
  width: 400px;
  padding: 8px;
  background-color: #f8b2b27d;
  border-radius: 5px;
  box-shadow: 0 2px 12px #ff7575a9, 0 0 0 8px #fff;
}

.shell input {
  width: 76%;
  height: 20px;
  color: #fff;
  font: 300 16px '优设标题黑';
  border: 0;
  background-color: transparent;
}

.shell input::placeholder {
  color: #eee8e8cb;
}

.shell a {
  display: flex;
  font-size: 24px;
  position: absolute;
  right: 8px;
  top: 4px;
  color: #fff;
  width: 62px;
  height: 37px;
}

.shell a .fa {
  margin: 2px 7px;
  transition: .3s;
}

.head-top .dropdown {
  display: block;
}

.shell a .fa-search {
  transform: translateX(-20px);
  opacity: 1;
}

.shell a .fa-hand-o-right {
  transform: translateX(-25px);
  opacity: 0;
}

.left-navi .hover-card .left .book-list .book-list-item {
  width: 160px;
  height: 29px;
  cursor: pointer;
  padding-top: 10px;
  padding-left: 10px;
  font-size: 13px;
  display: -webkit-box;
  color: #61666D;
  line-height: 29px;
  overflow: hidden;
  -webkit-line-clamp: 1;
}
.book-list-item:hover {
  background-color: #f0d7d7df;
  border-radius: 6%;

}


.shell .proshake:hover a .fa-search {
  transform: translateX(0);
  opacity: 0;
}
.hover-card {
  display: none;
  position: absolute;
  
  padding: 20px;
  width: 170px;
  height: 280px;
  border-radius: 8px;
  background-color: #fff;
  border: 1px solid #ccc;
}

.hover-me:hover ~ .hover-card,
.hover-card:hover {
  display: flex;
}

.shell .proshake:hover a .fa-hand-o-right {
  transform: translateX(22px);
  opacity: 1;
}

.shell a::before {
  content: 'GO!';
  position: absolute;
  display: block;
  font-size: 12px;
  background-color: #ff7575;
  padding: 1px 7px;
  top: 12px;
  right: 2px;
  border-radius: 2px;
  transition: .3s;
  opacity: 0;
  animation: box 1s infinite ease;
}

.shell .proshake:hover a::before {
  top: -22px;
  opacity: 1;
}

@keyframes box {
  0% {
    transform: rotate(0deg);
  }

  33% {
    transform: rotate(8deg);
  }

  66% {
    transform: rotate(-8deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

.clear path {
  position: relative;
  top: 2px;
  transition: fill .3s;
}

.clear:hover path {
  fill: #f8b2b2eb;
}

.login-avatar {
  --el-avatar-bg-color: #f56c6c;
  cursor: pointer;
}

.logininfo {
  margin: 16px 0 0 16px;
  font-size: 18px;
}

.login-button {
  margin-top: 12px;
  font-size: 16px;
  width: 100%;
  height: 42px;
}

.register {
  cursor: pointer;
  width: 100%;
  margin-top: 24px;
  display: flex;
  justify-content: center;
  font-size: 16px;
}

.register span a {
  margin-left: 8px;
  color: #f56c6c;
}
.icon{
  width: 30px;
  margin: 0 0 -25px 34px;
}
.login-pri {
  width: 100%;
  margin-top: 36px;
}

.login-pri li {
  font-size: 16px;
  width: 45%;
  float: left;
  margin: 0 0 24px 16px;
}

.login-pri li svg {
  margin-bottom: -4px;
  margin-right: 8px;
}


.edavatar {
  height: auto;
  background-color: transparent;
  position: relative;
  top: 0;
  right: 0;
  transition: all .3s ease-in-out;
  z-index: 100;
}

.edavatar:hover .el-avatar {
  box-shadow: 0 1px 20px rgba(0, 0, 0, .2);
}

.large {
  transform-origin: right top;
  transform: translateZ(0) scale(2);
}

.popuserinfo {
  transition: all .3s ease-in;
  position: absolute;
  z-index: 99;
}

.avatar {
  position: relative;
}

.proeffect .el-dialog {
  box-shadow: none;
  /* margin-top: 200px; */
}

.proeffect .el-dialog__headerbtn {
  left: 100%;
  top: -6px;
  margin-left: 64px;
  z-index: 1000;
}

.proeffect .el-dialog__headerbtn:focus .el-dialog__close,
.proeffect .el-dialog__headerbtn:hover .el-dialog__close {
  color: #f56c6c !important;
}

.left-navi,
.right-navi {
  display: flex;
  justify-content: center;
  width: 300px;
  /* height: 55px; */
}


.head-top .right-navi#fixmargin {
  width: 480px;
}

.head-top .right-navi#fixmargin .login-register {
  margin: 0 12px 0 48px;
}

.head-top .right-navi#fixmargin ul {
  display: flex;
  margin-right: 110px;
}

.left-navi a,
.right-navi ul li>a {
  width: 64px;
  display: flex;
  justify-content: center;
  line-height: 56px;
  height: 56px;
  /* color: #fff; */
  font-size: 16px;
  font-weight: 300;
  cursor: pointer;
  margin: 0;
  padding: 0 12px;
}

.left-navi a:hover,
.right-navi a:hover {
  animation: jump .3s;
}

@keyframes jump {
  0% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-3px);
  }

  100% {
    transform: translateY(0);
  }
}




.card{
    z-index:1 ;
    /* 相对定位 */
    position: relative;
    width: 300px;
    height: 450px;
    margin: 0 0 300px 50px;
    background-color: #758a99;
    border-radius: 20px;
    
    display: none;
    flex-direction: column;
    align-items: center;
    color: #fff;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
    flex-shrink: 0;

}
.card .photo img{
    width: 100%;
    height: 100%;
    /* 保持原有尺寸比例,裁切长边 */
    object-fit: cover;
}


.card .photo{
    /* 绝对定位 */
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    border-radius: 0%;
    overflow: hidden;
    transition: 0.5s;   
}


.card:hover .photo{
    top: 30px;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
}


.card .photo::before{
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom,transparent 50%,#222);
}

.card h1{
    position: absolute;
    top: 370px;
    font-size: 26px;
    transition: 0.5s;
}

.card:hover h1{
    top: 170px;
}

.card h2{
    margin-top: 220px;
    width: 80%;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
    font-size: 20px;
    text-align: center;
    margin-bottom: 20px;
    padding-bottom: 20px;
}

.card p {
    width: 90%;
    text-indent: 32px;
    font-size: 16px;
    margin-bottom: 15px;
    line-height: 30px;
}

.card a{
    font-size: 14px;
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    border: 1px solid rgba(255, 255, 255, 0.5);
    padding: 8px 32px;
    border-radius: 8px;
}
.card a:hover{
    color: #fff;
    background-color: rgba(255, 255, 255, 0.2);
}
.show-card{
  display: flex;
}
.close-icon{
  position: absolute;
  margin-left: 235px;
  top: 20px;
  cursor: pointer;
  
}
.closeicon{
  width: 20px;
transition: transform .4s ease-in-out;
}
.close-icon:hover .closeicon{
  transform: rotate(120deg);
}
</style>