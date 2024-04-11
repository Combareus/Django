(function() {
    var css = getBannerCss()
      , head = document.head || document.getElementsByTagName('head')[0]
      , style = document.createElement('style');
    style.type = 'text/css';
    if (style.styleSheet) {
        style.styleSheet.cssText = css;
    } else {
        style.appendChild(document.createTextNode(css));
    }
    head.appendChild(style);
    var bannerWrapper = document.getElementsByClassName('js-demo-avd')[0];
    bannerWrapper.innerHTML = getBannerHTML();
    bannerWrapper.addEventListener('click', function(event) {
        if (event.target.className == 'demo-avd__close') {
            event.preventDefault();
            bannerWrapper.setAttribute('style', 'display: none;');
            bannerWrapper.remove();
        }
    });
    function getBannerCss() {
        var style = '.demo-avd{position:fixed;width:200px;border-radius:.3em;overflow:hidden;-webkit-box-shadow:0 4px 20px rgba(0,0,0,.2);box-shadow:0 4px 20px rgba(0,0,0,.2);z-index:99;top:20px;right:20px;backdrop-filter:blur(10px)}.demo-avd--light{background-color:rgba(0,0,0,.8)}.demo-avd--dark{background-color:rgba(255,255,255,.8)}.demo-avd--light .demo-avd__template-text{color:#fff}.demo-avd--dark .demo-avd__template-img,.demo-avd--dark .demo-avd__template-text{color:rgba(0,0,0,.8)}.demo-avd .demo-avd__template-img{display:block;width:200px}.demo-avd .demo-avd__template-text{padding:10px;font-family:sans-serif!important}.demo-avd .demo-avd__template-text{font-size:14px;display:block;line-height:1.4;text-decoration:none}.demo-avd .demo-avd__template-text:hover{text-decoration:underline}.demo-avd .demo-avd__template-img img{display:block;width:200px}.demo-avd .demo-avd__template-text{text-decoration:none}.demo-avd__close{display:block;width:32px;height:32px;position:absolute;z-index:1;top:0;right:0;background:url(../../assets/img/icon-avd-close.svg) no-repeat 0 0;opacity:.8;cursor:auto}.demo-avd__close:hover{opacity:1}@media (max-width:800px){.demo-avd-cf{position:fixed;bottom:0!important;top:auto!important;left:0!important;right:0!important;width:100%!important;border-radius:0}.demo-avd-cf.demo-avd-cf--top-mb{top:0!important;bottom:auto!important}.demo-avd .demo-avd__template-img{display:none}.demo-avd .demo-avd__template-text{margin-top:2px}}';
        return style;
    }
    ;function getBannerHTML() {
        return '<div class="demo-avd__close"></div> <a href="https://nucleoapp.com/?ref=2214" class="demo-avd__template-img"> <img src="../../assets/img/sponsor/nucleo-adv-demo-1.jpg" alt="Nucleo logo"> </a> <a href="https://nucleoapp.com/?ref=2214" class="demo-avd__template-text"> Nucleo - Free icon manager for Mac and Windows</a>';
    }
    ;function loadAvdScript() {
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "//cdn.carbonads.com/carbon.js?serve=CKYIK2QE&placement=codyhouseco";
        script.id = "_carbonads_js";
        bannerWrapper.appendChild(script);
    }
    ;
}
)();
