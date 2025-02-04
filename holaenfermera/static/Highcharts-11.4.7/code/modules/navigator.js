!/**
 * Highcharts JS v11.4.7 (2024-08-14)
 *
 * Standalone navigator module
 *
 * (c) 2009-2024 Mateusz Bernacik
 *
 * License: www.highcharts.com/license
 */function(t){"object"==typeof module&&module.exports?(t.default=t,module.exports=t):"function"==typeof define&&define.amd?define("highcharts/modules/navigator",["highcharts"],function(i){return t(i),t.Highcharts=i,t}):t("undefined"!=typeof Highcharts?Highcharts:void 0)}(function(t){"use strict";var i=t?t._modules:{};function e(i,e,s,a){i.hasOwnProperty(e)||(i[e]=a.apply(null,s),"function"==typeof CustomEvent&&t.win.dispatchEvent(new CustomEvent("HighchartsModuleLoaded",{detail:{path:e,module:i[e]}})))}e(i,"Stock/Navigator/ChartNavigatorComposition.js",[i["Core/Globals.js"],i["Core/Utilities.js"]],function(t,i){let e;let{isTouchDevice:s}=t,{addEvent:a,merge:r,pick:o}=i,n=[];function h(){this.navigator&&this.navigator.setBaseSeries(null,!1)}function l(){let t,i,e;let s=this.legend,a=this.navigator;if(a){t=s&&s.options,i=a.xAxis,e=a.yAxis;let{scrollbarHeight:r,scrollButtonSize:n}=a;this.inverted?(a.left=a.opposite?this.chartWidth-r-a.height:this.spacing[3]+r,a.top=this.plotTop+n):(a.left=o(i.left,this.plotLeft+n),a.top=a.navigatorOptions.top||this.chartHeight-a.height-r-(this.scrollbar?.options.margin||0)-this.spacing[2]-(this.rangeSelector&&this.extraBottomMargin?this.rangeSelector.getHeight():0)-(t&&"bottom"===t.verticalAlign&&"proximate"!==t.layout&&t.enabled&&!t.floating?s.legendHeight+o(t.margin,10):0)-(this.titleOffset?this.titleOffset[2]:0)),i&&e&&(this.inverted?i.options.left=e.options.left=a.left:i.options.top=e.options.top=a.top,i.setAxisSize(),e.setAxisSize())}}function d(t){!this.navigator&&!this.scroller&&(this.options.navigator.enabled||this.options.scrollbar.enabled)&&(this.scroller=this.navigator=new e(this),o(t.redraw,!0)&&this.redraw(t.animation))}function c(){let t=this.options;(t.navigator.enabled||t.scrollbar.enabled)&&(this.scroller=this.navigator=new e(this))}function g(){let t=this.options,i=t.navigator,e=t.rangeSelector;if((i&&i.enabled||e&&e.enabled)&&(!s&&"x"===this.zooming.type||s&&"x"===this.zooming.pinchType))return!1}function p(t){let i=t.navigator;if(i&&t.xAxis[0]){let e=t.xAxis[0].getExtremes();i.render(e.min,e.max)}}function u(t){let i=t.options.navigator||{},e=t.options.scrollbar||{};!this.navigator&&!this.scroller&&(i.enabled||e.enabled)&&(r(!0,this.options.navigator,i),r(!0,this.options.scrollbar,e),delete t.options.navigator,delete t.options.scrollbar)}return{compose:function(t,s){if(i.pushUnique(n,t)){let i=t.prototype;e=s,i.callbacks.push(p),a(t,"afterAddSeries",h),a(t,"afterSetChartSize",l),a(t,"afterUpdate",d),a(t,"beforeRender",c),a(t,"beforeShowResetZoom",g),a(t,"update",u)}}}}),e(i,"Core/Axis/NavigatorAxisComposition.js",[i["Core/Globals.js"],i["Core/Utilities.js"]],function(t,i){let{isTouchDevice:e}=t,{addEvent:s,correctFloat:a,defined:r,isNumber:o,pick:n}=i;function h(){this.navigatorAxis||(this.navigatorAxis=new d(this))}function l(t){let i;let s=this.chart,a=s.options,o=a.navigator,n=this.navigatorAxis,h=s.zooming.pinchType,l=a.rangeSelector,d=s.zooming.type;if(this.isXAxis&&(o?.enabled||l?.enabled)){if("y"===d&&"zoom"===t.trigger)i=!1;else if(("zoom"===t.trigger&&"xy"===d||e&&"xy"===h)&&this.options.range){let i=n.previousZoom;r(t.min)?n.previousZoom=[this.min,this.max]:i&&(t.min=i[0],t.max=i[1],n.previousZoom=void 0)}}void 0!==i&&t.preventDefault()}class d{static compose(t){t.keepProps.includes("navigatorAxis")||(t.keepProps.push("navigatorAxis"),s(t,"init",h),s(t,"setExtremes",l))}constructor(t){this.axis=t}destroy(){this.axis=void 0}toFixedRange(t,i,e,s){let h=this.axis,l=(h.pointRange||0)/2,d=n(e,h.translate(t,!0,!h.horiz)),c=n(s,h.translate(i,!0,!h.horiz));return r(e)||(d=a(d+l)),r(s)||(c=a(c-l)),o(d)&&o(c)||(d=c=void 0),{min:d,max:c}}}return d}),e(i,"Stock/Navigator/NavigatorDefaults.js",[i["Core/Color/Color.js"],i["Core/Series/SeriesRegistry.js"]],function(t,i){let{parse:e}=t,{seriesTypes:s}=i;return{height:40,margin:25,maskInside:!0,handles:{width:7,borderRadius:0,height:15,symbols:["navigator-handle","navigator-handle"],enabled:!0,lineWidth:1,backgroundColor:"#f2f2f2",borderColor:"#999999"},maskFill:e("#667aff").setOpacity(.3).get(),outlineColor:"#999999",outlineWidth:1,series:{type:void 0===s.areaspline?"line":"areaspline",fillOpacity:.05,lineWidth:1,compare:null,sonification:{enabled:!1},dataGrouping:{approximation:"average",enabled:!0,groupPixelWidth:2,firstAnchor:"firstPoint",anchor:"middle",lastAnchor:"lastPoint",units:[["millisecond",[1,2,5,10,20,25,50,100,200,500]],["second",[1,2,5,10,15,30]],["minute",[1,2,5,10,15,30]],["hour",[1,2,3,4,6,8,12]],["day",[1,2,3,4]],["week",[1,2,3]],["month",[1,3,6]],["year",null]]},dataLabels:{enabled:!1,zIndex:2},id:"highcharts-navigator-series",className:"highcharts-navigator-series",lineColor:null,marker:{enabled:!1},threshold:null},xAxis:{className:"highcharts-navigator-xaxis",tickLength:0,lineWidth:0,gridLineColor:"#e6e6e6",id:"navigator-x-axis",gridLineWidth:1,tickPixelInterval:200,labels:{align:"left",style:{color:"#000000",fontSize:"0.7em",opacity:.6,textOutline:"2px contrast"},x:3,y:-4},crosshair:!1},yAxis:{className:"highcharts-navigator-yaxis",gridLineWidth:0,startOnTick:!1,endOnTick:!1,minPadding:.1,id:"navigator-y-axis",maxPadding:.1,labels:{enabled:!1},crosshair:!1,title:{text:null},tickLength:0,tickWidth:0}}}),e(i,"Stock/Navigator/NavigatorSymbols.js",[i["Core/Renderer/SVG/Symbols.js"],i["Core/Utilities.js"]],function(t,i){let{relativeLength:e}=i;return{"navigator-handle":function(i,s,a,r,o={}){let n=o.width?o.width/2:a,h=e(o.borderRadius||0,Math.min(2*n,r));return[["M",-1.5,(r=o.height||r)/2-3.5],["L",-1.5,r/2+4.5],["M",.5,r/2-3.5],["L",.5,r/2+4.5],...t.rect(-n-1,.5,2*n+1,r,{r:h})]}}}),e(i,"Stock/Utilities/StockUtilities.js",[i["Core/Utilities.js"]],function(t){let{defined:i}=t;return{setFixedRange:function(t){let e=this.xAxis[0];i(e.dataMax)&&i(e.dataMin)&&t?this.fixedRange=Math.min(t,e.dataMax-e.dataMin):this.fixedRange=t}}}),e(i,"Stock/Navigator/NavigatorComposition.js",[i["Core/Defaults.js"],i["Core/Globals.js"],i["Core/Axis/NavigatorAxisComposition.js"],i["Stock/Navigator/NavigatorDefaults.js"],i["Stock/Navigator/NavigatorSymbols.js"],i["Core/Renderer/RendererRegistry.js"],i["Stock/Utilities/StockUtilities.js"],i["Core/Utilities.js"]],function(t,i,e,s,a,r,o,n){let{setOptions:h}=t,{composed:l}=i,{getRendererType:d}=r,{setFixedRange:c}=o,{addEvent:g,extend:p,pushUnique:u}=n;function x(){this.chart.navigator&&!this.options.isInternal&&this.chart.navigator.setBaseSeries(null,!1)}return{compose:function(t,i,r){e.compose(i),u(l,"Navigator")&&(t.prototype.setFixedRange=c,p(d().prototype.symbols,a),g(r,"afterUpdate",x),h({navigator:s}))}}}),e(i,"Core/Axis/ScrollbarAxis.js",[i["Core/Globals.js"],i["Core/Utilities.js"]],function(t,i){var e;let{composed:s}=t,{addEvent:a,defined:r,pick:o,pushUnique:n}=i;return function(t){let i;function e(t){let i=o(t.options&&t.options.min,t.min),e=o(t.options&&t.options.max,t.max);return{axisMin:i,axisMax:e,scrollMin:r(t.dataMin)?Math.min(i,t.min,t.dataMin,o(t.threshold,1/0)):i,scrollMax:r(t.dataMax)?Math.max(e,t.max,t.dataMax,o(t.threshold,-1/0)):e}}function h(){let t=this.scrollbar,i=t&&!t.options.opposite,e=this.horiz?2:i?3:1;t&&(this.chart.scrollbarsOffsets=[0,0],this.chart.axisOffset[e]+=t.size+(t.options.margin||0))}function l(){let t=this;t.options&&t.options.scrollbar&&t.options.scrollbar.enabled&&(t.options.scrollbar.vertical=!t.horiz,t.options.startOnTick=t.options.endOnTick=!1,t.scrollbar=new i(t.chart.renderer,t.options.scrollbar,t.chart),a(t.scrollbar,"changed",function(i){let s,a;let{axisMin:o,axisMax:n,scrollMin:h,scrollMax:l}=e(t),d=l-h;if(r(o)&&r(n)){if(t.horiz&&!t.reversed||!t.horiz&&t.reversed?(s=h+d*this.to,a=h+d*this.from):(s=h+d*(1-this.from),a=h+d*(1-this.to)),this.shouldUpdateExtremes(i.DOMType)){let e="mousemove"!==i.DOMType&&"touchmove"!==i.DOMType&&void 0;t.setExtremes(a,s,!0,e,i)}else this.setRange(this.from,this.to)}}))}function d(){let t,i,s;let{scrollMin:a,scrollMax:o}=e(this),n=this.scrollbar,h=this.axisTitleMargin+(this.titleOffset||0),l=this.chart.scrollbarsOffsets,d=this.options.margin||0;if(n&&l){if(this.horiz)this.opposite||(l[1]+=h),n.position(this.left,this.top+this.height+2+l[1]-(this.opposite?d:0),this.width,this.height),this.opposite||(l[1]+=d),t=1;else{let i;this.opposite&&(l[0]+=h),i=n.options.opposite?this.left+this.width+2+l[0]-(this.opposite?0:d):this.opposite?0:d,n.position(i,this.top,this.width,this.height),this.opposite&&(l[0]+=d),t=0}l[t]+=n.size+(n.options.margin||0),isNaN(a)||isNaN(o)||!r(this.min)||!r(this.max)||this.min===this.max?n.setRange(0,1):(i=(this.min-a)/(o-a),s=(this.max-a)/(o-a),this.horiz&&!this.reversed||!this.horiz&&this.reversed?n.setRange(i,s):n.setRange(1-s,1-i))}}t.compose=function(t,e){n(s,"Axis.Scrollbar")&&(i=e,a(t,"afterGetOffset",h),a(t,"afterInit",l),a(t,"afterRender",d))}}(e||(e={})),e}),e(i,"Stock/Scrollbar/ScrollbarDefaults.js",[],function(){return{height:10,barBorderRadius:5,buttonBorderRadius:0,buttonsEnabled:!1,liveRedraw:void 0,margin:void 0,minWidth:6,opposite:!0,step:.2,zIndex:3,barBackgroundColor:"#cccccc",barBorderWidth:0,barBorderColor:"#cccccc",buttonArrowColor:"#333333",buttonBackgroundColor:"#e6e6e6",buttonBorderColor:"#cccccc",buttonBorderWidth:1,rifleColor:"none",trackBackgroundColor:"rgba(255, 255, 255, 0.001)",trackBorderColor:"#cccccc",trackBorderRadius:5,trackBorderWidth:1}}),e(i,"Stock/Scrollbar/Scrollbar.js",[i["Core/Defaults.js"],i["Core/Globals.js"],i["Core/Axis/ScrollbarAxis.js"],i["Stock/Scrollbar/ScrollbarDefaults.js"],i["Core/Utilities.js"]],function(t,i,e,s,a){let{defaultOptions:r}=t,{addEvent:o,correctFloat:n,crisp:h,defined:l,destroyObjectProperties:d,fireEvent:c,merge:g,pick:p,removeEvent:u}=a;class x{static compose(t){e.compose(t,x)}static swapXY(t,i){return i&&t.forEach(t=>{let i;let e=t.length;for(let s=0;s<e;s+=2)"number"==typeof(i=t[s+1])&&(t[s+1]=t[s+2],t[s+2]=i)}),t}constructor(t,i,e){this._events=[],this.chartX=0,this.chartY=0,this.from=0,this.scrollbarButtons=[],this.scrollbarLeft=0,this.scrollbarStrokeWidth=1,this.scrollbarTop=0,this.size=0,this.to=0,this.trackBorderWidth=1,this.x=0,this.y=0,this.init(t,i,e)}addEvents(){let t=this.options.inverted?[1,0]:[0,1],i=this.scrollbarButtons,e=this.scrollbarGroup.element,s=this.track.element,a=this.mouseDownHandler.bind(this),r=this.mouseMoveHandler.bind(this),n=this.mouseUpHandler.bind(this),h=[[i[t[0]].element,"click",this.buttonToMinClick.bind(this)],[i[t[1]].element,"click",this.buttonToMaxClick.bind(this)],[s,"click",this.trackClick.bind(this)],[e,"mousedown",a],[e.ownerDocument,"mousemove",r],[e.ownerDocument,"mouseup",n],[e,"touchstart",a],[e.ownerDocument,"touchmove",r],[e.ownerDocument,"touchend",n]];h.forEach(function(t){o.apply(null,t)}),this._events=h}buttonToMaxClick(t){let i=(this.to-this.from)*p(this.options.step,.2);this.updatePosition(this.from+i,this.to+i),c(this,"changed",{from:this.from,to:this.to,trigger:"scrollbar",DOMEvent:t})}buttonToMinClick(t){let i=n(this.to-this.from)*p(this.options.step,.2);this.updatePosition(n(this.from-i),n(this.to-i)),c(this,"changed",{from:this.from,to:this.to,trigger:"scrollbar",DOMEvent:t})}cursorToScrollbarPosition(t){let i=this.options,e=i.minWidth>this.calculatedWidth?i.minWidth:0;return{chartX:(t.chartX-this.x-this.xOffset)/(this.barWidth-e),chartY:(t.chartY-this.y-this.yOffset)/(this.barWidth-e)}}destroy(){let t=this,i=t.chart.scroller;t.removeEvents(),["track","scrollbarRifles","scrollbar","scrollbarGroup","group"].forEach(function(i){t[i]&&t[i].destroy&&(t[i]=t[i].destroy())}),i&&t===i.scrollbar&&(i.scrollbar=null,d(i.scrollbarButtons))}drawScrollbarButton(t){let i=this.renderer,e=this.scrollbarButtons,s=this.options,a=this.size,r=i.g().add(this.group);if(e.push(r),s.buttonsEnabled){let o=i.rect().addClass("highcharts-scrollbar-button").add(r);this.chart.styledMode||o.attr({stroke:s.buttonBorderColor,"stroke-width":s.buttonBorderWidth,fill:s.buttonBackgroundColor}),o.attr(o.crisp({x:-.5,y:-.5,width:a,height:a,r:s.buttonBorderRadius},o.strokeWidth()));let n=i.path(x.swapXY([["M",a/2+(t?-1:1),a/2-3],["L",a/2+(t?-1:1),a/2+3],["L",a/2+(t?2:-2),a/2]],s.vertical)).addClass("highcharts-scrollbar-arrow").add(e[t]);this.chart.styledMode||n.attr({fill:s.buttonArrowColor})}}init(t,i,e){this.scrollbarButtons=[],this.renderer=t,this.userOptions=i,this.options=g(s,r.scrollbar,i),this.options.margin=p(this.options.margin,10),this.chart=e,this.size=p(this.options.size,this.options.height),i.enabled&&(this.render(),this.addEvents())}mouseDownHandler(t){let i=this.chart.pointer?.normalize(t)||t,e=this.cursorToScrollbarPosition(i);this.chartX=e.chartX,this.chartY=e.chartY,this.initPositions=[this.from,this.to],this.grabbedCenter=!0}mouseMoveHandler(t){let i;let e=this.chart.pointer?.normalize(t)||t,s=this.options.vertical?"chartY":"chartX",a=this.initPositions||[];this.grabbedCenter&&(!t.touches||0!==t.touches[0][s])&&(i=this.cursorToScrollbarPosition(e)[s]-this[s],this.hasDragged=!0,this.updatePosition(a[0]+i,a[1]+i),this.hasDragged&&c(this,"changed",{from:this.from,to:this.to,trigger:"scrollbar",DOMType:t.type,DOMEvent:t}))}mouseUpHandler(t){this.hasDragged&&c(this,"changed",{from:this.from,to:this.to,trigger:"scrollbar",DOMType:t.type,DOMEvent:t}),this.grabbedCenter=this.hasDragged=this.chartX=this.chartY=null}position(t,i,e,s){let{buttonsEnabled:a,margin:r=0,vertical:o}=this.options,n=this.rendered?"animate":"attr",h=s,l=0;this.group.show(),this.x=t,this.y=i+this.trackBorderWidth,this.width=e,this.height=s,this.xOffset=h,this.yOffset=l,o?(this.width=this.yOffset=e=l=this.size,this.xOffset=h=0,this.yOffset=l=a?this.size:0,this.barWidth=s-(a?2*e:0),this.x=t+=r):(this.height=s=this.size,this.xOffset=h=a?this.size:0,this.barWidth=e-(a?2*s:0),this.y=this.y+r),this.group[n]({translateX:t,translateY:this.y}),this.track[n]({width:e,height:s}),this.scrollbarButtons[1][n]({translateX:o?0:e-h,translateY:o?s-l:0})}removeEvents(){this._events.forEach(function(t){u.apply(null,t)}),this._events.length=0}render(){let t=this.renderer,i=this.options,e=this.size,s=this.chart.styledMode,a=t.g("scrollbar").attr({zIndex:i.zIndex}).hide().add();this.group=a,this.track=t.rect().addClass("highcharts-scrollbar-track").attr({r:i.trackBorderRadius||0,height:e,width:e}).add(a),s||this.track.attr({fill:i.trackBackgroundColor,stroke:i.trackBorderColor,"stroke-width":i.trackBorderWidth});let r=this.trackBorderWidth=this.track.strokeWidth();this.track.attr({x:-h(0,r),y:-h(0,r)}),this.scrollbarGroup=t.g().add(a),this.scrollbar=t.rect().addClass("highcharts-scrollbar-thumb").attr({height:e-r,width:e-r,r:i.barBorderRadius||0}).add(this.scrollbarGroup),this.scrollbarRifles=t.path(x.swapXY([["M",-3,e/4],["L",-3,2*e/3],["M",0,e/4],["L",0,2*e/3],["M",3,e/4],["L",3,2*e/3]],i.vertical)).addClass("highcharts-scrollbar-rifles").add(this.scrollbarGroup),s||(this.scrollbar.attr({fill:i.barBackgroundColor,stroke:i.barBorderColor,"stroke-width":i.barBorderWidth}),this.scrollbarRifles.attr({stroke:i.rifleColor,"stroke-width":1})),this.scrollbarStrokeWidth=this.scrollbar.strokeWidth(),this.scrollbarGroup.translate(-h(0,this.scrollbarStrokeWidth),-h(0,this.scrollbarStrokeWidth)),this.drawScrollbarButton(0),this.drawScrollbarButton(1)}setRange(t,i){let e,s;let a=this.options,r=a.vertical,o=a.minWidth,h=this.barWidth,d=!this.rendered||this.hasDragged||this.chart.navigator&&this.chart.navigator.hasDragged?"attr":"animate";if(!l(h))return;let c=h*Math.min(i,1);e=Math.ceil(h*(t=Math.max(t,0))),this.calculatedWidth=s=n(c-e),s<o&&(e=(h-o+s)*t,s=o);let g=Math.floor(e+this.xOffset+this.yOffset),p=s/2-.5;this.from=t,this.to=i,r?(this.scrollbarGroup[d]({translateY:g}),this.scrollbar[d]({height:s}),this.scrollbarRifles[d]({translateY:p}),this.scrollbarTop=g,this.scrollbarLeft=0):(this.scrollbarGroup[d]({translateX:g}),this.scrollbar[d]({width:s}),this.scrollbarRifles[d]({translateX:p}),this.scrollbarLeft=g,this.scrollbarTop=0),s<=12?this.scrollbarRifles.hide():this.scrollbarRifles.show(),!1===a.showFull&&(t<=0&&i>=1?this.group.hide():this.group.show()),this.rendered=!0}shouldUpdateExtremes(t){return p(this.options.liveRedraw,i.svg&&!i.isTouchDevice&&!this.chart.boosted)||"mouseup"===t||"touchend"===t||!l(t)}trackClick(t){let i=this.chart.pointer?.normalize(t)||t,e=this.to-this.from,s=this.y+this.scrollbarTop,a=this.x+this.scrollbarLeft;this.options.vertical&&i.chartY>s||!this.options.vertical&&i.chartX>a?this.updatePosition(this.from+e,this.to+e):this.updatePosition(this.from-e,this.to-e),c(this,"changed",{from:this.from,to:this.to,trigger:"scrollbar",DOMEvent:t})}update(t){this.destroy(),this.init(this.chart.renderer,g(!0,this.options,t),this.chart)}updatePosition(t,i){i>1&&(t=n(1-n(i-t)),i=1),t<0&&(i=n(i-t),t=0),this.from=t,this.to=i}}return x.defaultOptions=s,r.scrollbar=g(!0,x.defaultOptions,r.scrollbar),x}),e(i,"Stock/Navigator/Navigator.js",[i["Core/Axis/Axis.js"],i["Stock/Navigator/ChartNavigatorComposition.js"],i["Core/Defaults.js"],i["Core/Globals.js"],i["Core/Axis/NavigatorAxisComposition.js"],i["Stock/Navigator/NavigatorComposition.js"],i["Stock/Scrollbar/Scrollbar.js"],i["Core/Renderer/SVG/SVGRenderer.js"],i["Core/Utilities.js"]],function(t,i,e,s,a,r,o,n,h){let{defaultOptions:l}=e,{isTouchDevice:d}=s,{prototype:{symbols:c}}=n,{addEvent:g,clamp:p,correctFloat:u,defined:x,destroyObjectProperties:m,erase:v,extend:b,find:f,fireEvent:M,isArray:A,isNumber:S,merge:y,pick:k,removeEvent:E,splat:w}=h;function C(t,...i){let e=[].filter.call(i,S);if(e.length)return Math[t].apply(0,e)}class O{static compose(t,e,s){i.compose(t,O),r.compose(t,e,s)}constructor(t){this.isDirty=!1,this.scrollbarHeight=0,this.init(t)}drawHandle(t,i,e,s){let a=this.navigatorOptions.handles.height;this.handles[i][s](e?{translateX:Math.round(this.left+this.height/2),translateY:Math.round(this.top+parseInt(t,10)+.5-a)}:{translateX:Math.round(this.left+parseInt(t,10)),translateY:Math.round(this.top+this.height/2-a/2-1)})}drawOutline(t,i,e,s){let a=this.navigatorOptions.maskInside,r=this.outline.strokeWidth(),o=r/2,n=r%2/2,h=this.scrollButtonSize,l=this.size,d=this.top,c=this.height,g=d-o,p=d+c,u=this.left,x,m;e?(x=d+i+n,i=d+t+n,m=[["M",u+c,d-h-n],["L",u+c,x],["L",u,x],["M",u,i],["L",u+c,i],["L",u+c,d+l+h]],a&&m.push(["M",u+c,x-o],["L",u+c,i+o])):(u-=h,t+=u+h-n,i+=u+h-n,m=[["M",u,g],["L",t,g],["L",t,p],["M",i,p],["L",i,g],["L",u+l+2*h,g]],a&&m.push(["M",t-o,g],["L",i+o,g])),this.outline[s]({d:m})}drawMasks(t,i,e,s){let a,r,o,n;let h=this.left,l=this.top,d=this.height;e?(o=[h,h,h],n=[l,l+t,l+i],r=[d,d,d],a=[t,i-t,this.size-i]):(o=[h,h+t,h+i],n=[l,l,l],r=[t,i-t,this.size-i],a=[d,d,d]),this.shades.forEach((t,i)=>{t[s]({x:o[i],y:n[i],width:r[i],height:a[i]})})}renderElements(){let t=this,i=t.navigatorOptions,e=i.maskInside,s=t.chart,a=s.inverted,r=s.renderer,o={cursor:a?"ns-resize":"ew-resize"},n=t.navigatorGroup??(t.navigatorGroup=r.g("navigator").attr({zIndex:8,visibility:"hidden"}).add());if([!e,e,!e].forEach((e,a)=>{let h=t.shades[a]??(t.shades[a]=r.rect().addClass("highcharts-navigator-mask"+(1===a?"-inside":"-outside")).add(n));s.styledMode||(h.attr({fill:e?i.maskFill:"rgba(0,0,0,0)"}),1===a&&h.css(o))}),t.outline||(t.outline=r.path().addClass("highcharts-navigator-outline").add(n)),s.styledMode||t.outline.attr({"stroke-width":i.outlineWidth,stroke:i.outlineColor}),i.handles?.enabled){let e=i.handles,{height:a,width:h}=e;[0,1].forEach(i=>{let l=e.symbols[i];if(t.handles[i]){if(l!==t.handles[i].symbolName){let e=c[l].call(c,-h/2-1,0,h,a);t.handles[i].attr({d:e}),t.handles[i].symbolName=l}}else t.handles[i]=r.symbol(l,-h/2-1,0,h,a,e),t.handles[i].attr({zIndex:7-i}).addClass("highcharts-navigator-handle highcharts-navigator-handle-"+["left","right"][i]).add(n);s.inverted&&t.handles[i].attr({rotation:90,rotationOriginX:Math.floor(-h/2),rotationOriginY:(a+h)/2}),s.styledMode||t.handles[i].attr({fill:e.backgroundColor,stroke:e.borderColor,"stroke-width":e.lineWidth,width:e.width,height:e.height,x:-h/2-1,y:0}).css(o)})}}update(t,i=!1){let e=this.chart,s=e.options.chart.inverted!==e.scrollbar?.options.vertical;if(y(!0,e.options.navigator,t),this.navigatorOptions=e.options.navigator||{},this.setOpposite(),x(t.enabled)||s)return this.destroy(),this.navigatorEnabled=t.enabled||this.navigatorEnabled,this.init(e);if(this.navigatorEnabled&&(this.isDirty=!0,!1===t.adaptToUpdatedData&&this.baseSeries.forEach(t=>{E(t,"updatedData",this.updatedDataHandler)},this),t.adaptToUpdatedData&&this.baseSeries.forEach(t=>{t.eventsToUnbind.push(g(t,"updatedData",this.updatedDataHandler))},this),(t.series||t.baseSeries)&&this.setBaseSeries(void 0,!1),t.height||t.xAxis||t.yAxis)){this.height=t.height??this.height;let i=this.getXAxisOffsets();this.xAxis.update({...t.xAxis,offsets:i,[e.inverted?"width":"height"]:this.height,[e.inverted?"height":"width"]:void 0},!1),this.yAxis.update({...t.yAxis,[e.inverted?"width":"height"]:this.height},!1)}i&&e.redraw()}render(t,i,e,s){let a=this.chart,r=this.xAxis,o=r.pointRange||0,n=r.navigatorAxis.fake?a.xAxis[0]:r,h=this.navigatorEnabled,l=this.rendered,d=a.inverted,c=a.xAxis[0].minRange,g=a.xAxis[0].options.maxRange,m=this.scrollButtonSize,v,b,f,A=this.scrollbarHeight,y,E;if(this.hasDragged&&!x(e))return;if(this.isDirty&&this.renderElements(),t=u(t-o/2),i=u(i+o/2),!S(t)||!S(i)){if(!l)return;e=0,s=k(r.width,n.width)}this.left=k(r.left,a.plotLeft+m+(d?a.plotWidth:0));let w=this.size=y=k(r.len,(d?a.plotHeight:a.plotWidth)-2*m);v=d?A:y+2*m,e=k(e,r.toPixels(t,!0)),s=k(s,r.toPixels(i,!0)),S(e)&&Math.abs(e)!==1/0||(e=0,s=v);let C=r.toValue(e,!0),O=r.toValue(s,!0),D=Math.abs(u(O-C));D<c?this.grabbedLeft?e=r.toPixels(O-c-o,!0):this.grabbedRight&&(s=r.toPixels(C+c+o,!0)):x(g)&&u(D-o)>g&&(this.grabbedLeft?e=r.toPixels(O-g-o,!0):this.grabbedRight&&(s=r.toPixels(C+g+o,!0))),this.zoomedMax=p(Math.max(e,s),0,w),this.zoomedMin=p(this.fixedWidth?this.zoomedMax-this.fixedWidth:Math.min(e,s),0,w),this.range=this.zoomedMax-this.zoomedMin,w=Math.round(this.zoomedMax);let z=Math.round(this.zoomedMin);h&&(this.navigatorGroup.attr({visibility:"inherit"}),E=l&&!this.hasDragged?"animate":"attr",this.drawMasks(z,w,d,E),this.drawOutline(z,w,d,E),this.navigatorOptions.handles.enabled&&(this.drawHandle(z,0,d,E),this.drawHandle(w,1,d,E))),this.scrollbar&&(d?(f=this.top-m,b=this.left-A+(h||!n.opposite?0:(n.titleOffset||0)+n.axisTitleMargin),A=y+2*m):(f=this.top+(h?this.height:-A),b=this.left-m),this.scrollbar.position(b,f,v,A),this.scrollbar.setRange(this.zoomedMin/(y||1),this.zoomedMax/(y||1))),this.rendered=!0,this.isDirty=!1,M(this,"afterRender")}addMouseEvents(){let t=this,i=t.chart,e=i.container,s=[],a,r;t.mouseMoveHandler=a=function(i){t.onMouseMove(i)},t.mouseUpHandler=r=function(i){t.onMouseUp(i)},(s=t.getPartsEvents("mousedown")).push(g(i.renderTo,"mousemove",a),g(e.ownerDocument,"mouseup",r),g(i.renderTo,"touchmove",a),g(e.ownerDocument,"touchend",r)),s.concat(t.getPartsEvents("touchstart")),t.eventsToUnbind=s,t.series&&t.series[0]&&s.push(g(t.series[0].xAxis,"foundExtremes",function(){i.navigator.modifyNavigatorAxisExtremes()}))}getPartsEvents(t){let i=this,e=[];return["shades","handles"].forEach(function(s){i[s].forEach(function(a,r){e.push(g(a.element,t,function(t){i[s+"Mousedown"](t,r)}))})}),e}shadesMousedown(t,i){t=this.chart.pointer?.normalize(t)||t;let e=this.chart,s=this.xAxis,a=this.zoomedMin,r=this.size,o=this.range,n=this.left,h=t.chartX,l,d,c,g;e.inverted&&(h=t.chartY,n=this.top),1===i?(this.grabbedCenter=h,this.fixedWidth=o,this.dragOffset=h-a):(g=h-n-o/2,0===i?g=Math.max(0,g):2===i&&g+o>=r&&(g=r-o,this.reversedExtremes?(g-=o,d=this.getUnionExtremes().dataMin):l=this.getUnionExtremes().dataMax),g!==a&&(this.fixedWidth=o,x((c=s.navigatorAxis.toFixedRange(g,g+o,d,l)).min)&&M(this,"setRange",{min:Math.min(c.min,c.max),max:Math.max(c.min,c.max),redraw:!0,eventArguments:{trigger:"navigator"}})))}handlesMousedown(t,i){t=this.chart.pointer?.normalize(t)||t;let e=this.chart,s=e.xAxis[0],a=this.reversedExtremes;0===i?(this.grabbedLeft=!0,this.otherHandlePos=this.zoomedMax,this.fixedExtreme=a?s.min:s.max):(this.grabbedRight=!0,this.otherHandlePos=this.zoomedMin,this.fixedExtreme=a?s.max:s.min),e.setFixedRange(void 0)}onMouseMove(t){let i=this,e=i.chart,s=i.navigatorSize,a=i.range,r=i.dragOffset,o=e.inverted,n=i.left,h;(!t.touches||0!==t.touches[0].pageX)&&(h=(t=e.pointer?.normalize(t)||t).chartX,o&&(n=i.top,h=t.chartY),i.grabbedLeft?(i.hasDragged=!0,i.render(0,0,h-n,i.otherHandlePos)):i.grabbedRight?(i.hasDragged=!0,i.render(0,0,i.otherHandlePos,h-n)):i.grabbedCenter&&(i.hasDragged=!0,h<r?h=r:h>s+r-a&&(h=s+r-a),i.render(0,0,h-r,h-r+a)),i.hasDragged&&i.scrollbar&&k(i.scrollbar.options.liveRedraw,!d&&!this.chart.boosted)&&(t.DOMType=t.type,setTimeout(function(){i.onMouseUp(t)},0)))}onMouseUp(t){let i,e,s,a,r,o;let n=this.chart,h=this.xAxis,l=this.scrollbar,d=t.DOMEvent||t,c=n.inverted,g=this.rendered&&!this.hasDragged?"animate":"attr";(this.hasDragged&&(!l||!l.hasDragged)||"scrollbar"===t.trigger)&&(s=this.getUnionExtremes(),this.zoomedMin===this.otherHandlePos?a=this.fixedExtreme:this.zoomedMax===this.otherHandlePos&&(r=this.fixedExtreme),this.zoomedMax===this.size&&(r=this.reversedExtremes?s.dataMin:s.dataMax),0===this.zoomedMin&&(a=this.reversedExtremes?s.dataMax:s.dataMin),x((o=h.navigatorAxis.toFixedRange(this.zoomedMin,this.zoomedMax,a,r)).min)&&M(this,"setRange",{min:Math.min(o.min,o.max),max:Math.max(o.min,o.max),redraw:!0,animation:!this.hasDragged&&null,eventArguments:{trigger:"navigator",triggerOp:"navigator-drag",DOMEvent:d}})),"mousemove"!==t.DOMType&&"touchmove"!==t.DOMType&&(this.grabbedLeft=this.grabbedRight=this.grabbedCenter=this.fixedWidth=this.fixedExtreme=this.otherHandlePos=this.hasDragged=this.dragOffset=null),this.navigatorEnabled&&S(this.zoomedMin)&&S(this.zoomedMax)&&(e=Math.round(this.zoomedMin),i=Math.round(this.zoomedMax),this.shades&&this.drawMasks(e,i,c,g),this.outline&&this.drawOutline(e,i,c,g),this.navigatorOptions.handles.enabled&&Object.keys(this.handles).length===this.handles.length&&(this.drawHandle(e,0,c,g),this.drawHandle(i,1,c,g)))}removeEvents(){this.eventsToUnbind&&(this.eventsToUnbind.forEach(function(t){t()}),this.eventsToUnbind=void 0),this.removeBaseSeriesEvents()}removeBaseSeriesEvents(){let t=this.baseSeries||[];this.navigatorEnabled&&t[0]&&(!1!==this.navigatorOptions.adaptToUpdatedData&&t.forEach(function(t){E(t,"updatedData",this.updatedDataHandler)},this),t[0].xAxis&&E(t[0].xAxis,"foundExtremes",this.modifyBaseAxisExtremes))}getXAxisOffsets(){return this.chart.inverted?[this.scrollButtonSize,0,-this.scrollButtonSize,0]:[0,-this.scrollButtonSize,0,this.scrollButtonSize]}init(i){let e=i.options,s=e.navigator||{},r=s.enabled,n=e.scrollbar||{},h=n.enabled,l=r&&s.height||0,d=h&&n.height||0,c=n.buttonsEnabled&&d||0;this.handles=[],this.shades=[],this.chart=i,this.setBaseSeries(),this.height=l,this.scrollbarHeight=d,this.scrollButtonSize=c,this.scrollbarEnabled=h,this.navigatorEnabled=r,this.navigatorOptions=s,this.scrollbarOptions=n,this.setOpposite();let p=this,u=p.baseSeries,x=i.xAxis.length,m=i.yAxis.length,v=u&&u[0]&&u[0].xAxis||i.xAxis[0]||{options:{}};if(i.isDirtyBox=!0,p.navigatorEnabled){let e=this.getXAxisOffsets();p.xAxis=new t(i,y({breaks:v.options.breaks,ordinal:v.options.ordinal,overscroll:v.options.overscroll},s.xAxis,{type:"datetime",yAxis:s.yAxis?.id,index:x,isInternal:!0,offset:0,keepOrdinalPadding:!0,startOnTick:!1,endOnTick:!1,minPadding:v.options.ordinal?0:v.options.minPadding,maxPadding:v.options.ordinal?0:v.options.maxPadding,zoomEnabled:!1},i.inverted?{offsets:e,width:l}:{offsets:e,height:l}),"xAxis"),p.yAxis=new t(i,y(s.yAxis,{alignTicks:!1,offset:0,index:m,isInternal:!0,reversed:k(s.yAxis&&s.yAxis.reversed,i.yAxis[0]&&i.yAxis[0].reversed,!1),zoomEnabled:!1},i.inverted?{width:l}:{height:l}),"yAxis"),u||s.series.data?p.updateNavigatorSeries(!1):0===i.series.length&&(p.unbindRedraw=g(i,"beforeRedraw",function(){i.series.length>0&&!p.series&&(p.setBaseSeries(),p.unbindRedraw())})),p.reversedExtremes=i.inverted&&!p.xAxis.reversed||!i.inverted&&p.xAxis.reversed,p.renderElements(),p.addMouseEvents()}else p.xAxis={chart:i,navigatorAxis:{fake:!0},translate:function(t,e){let s=i.xAxis[0],a=s.getExtremes(),r=s.len-2*c,o=C("min",s.options.min,a.dataMin),n=C("max",s.options.max,a.dataMax)-o;return e?t*n/r+o:r*(t-o)/n},toPixels:function(t){return this.translate(t)},toValue:function(t){return this.translate(t,!0)}},p.xAxis.navigatorAxis.axis=p.xAxis,p.xAxis.navigatorAxis.toFixedRange=a.prototype.toFixedRange.bind(p.xAxis.navigatorAxis);if(i.options.scrollbar.enabled){let t=y(i.options.scrollbar,{vertical:i.inverted});!S(t.margin)&&p.navigatorEnabled&&(t.margin=i.inverted?-3:3),i.scrollbar=p.scrollbar=new o(i.renderer,t,i),g(p.scrollbar,"changed",function(t){let i=p.size,e=i*this.to,s=i*this.from;p.hasDragged=p.scrollbar.hasDragged,p.render(0,0,s,e),this.shouldUpdateExtremes(t.DOMType)&&setTimeout(function(){p.onMouseUp(t)})})}p.addBaseSeriesEvents(),p.addChartEvents()}setOpposite(){let t=this.navigatorOptions,i=this.navigatorEnabled,e=this.chart;this.opposite=k(t.opposite,!!(!i&&e.inverted))}getUnionExtremes(t){let i;let e=this.chart.xAxis[0],s=this.xAxis,a=s.options,r=e.options;return t&&null===e.dataMin||(i={dataMin:k(a&&a.min,C("min",r.min,e.dataMin,s.dataMin,s.min)),dataMax:k(a&&a.max,C("max",r.max,e.dataMax,s.dataMax,s.max))}),i}setBaseSeries(t,i){let e=this.chart,s=this.baseSeries=[];t=t||e.options&&e.options.navigator.baseSeries||(e.series.length?f(e.series,t=>!t.options.isInternal).index:0),(e.series||[]).forEach((i,e)=>{!i.options.isInternal&&(i.options.showInNavigator||(e===t||i.options.id===t)&&!1!==i.options.showInNavigator)&&s.push(i)}),this.xAxis&&!this.xAxis.navigatorAxis.fake&&this.updateNavigatorSeries(!0,i)}updateNavigatorSeries(t,i){let e=this,s=e.chart,a=e.baseSeries,r={enableMouseTracking:!1,index:null,linkedTo:null,group:"nav",padXAxis:!1,xAxis:this.navigatorOptions.xAxis?.id,yAxis:this.navigatorOptions.yAxis?.id,showInLegend:!1,stacking:void 0,isInternal:!0,states:{inactive:{opacity:1}}},o=e.series=(e.series||[]).filter(t=>{let i=t.baseSeries;return!(0>a.indexOf(i))||(i&&(E(i,"updatedData",e.updatedDataHandler),delete i.navigatorSeries),t.chart&&t.destroy(),!1)}),n,h,d=e.navigatorOptions.series,c;a&&a.length&&a.forEach(t=>{let g=t.navigatorSeries,p=b({color:t.color,visible:t.visible},A(d)?l.navigator.series:d);if(g&&!1===e.navigatorOptions.adaptToUpdatedData)return;r.name="Navigator "+a.length,c=(n=t.options||{}).navigatorOptions||{},p.dataLabels=w(p.dataLabels),(h=y(n,r,p,c)).pointRange=k(p.pointRange,c.pointRange,l.plotOptions[h.type||"line"].pointRange);let u=c.data||p.data;e.hasNavigatorData=e.hasNavigatorData||!!u,h.data=u||n.data&&n.data.slice(0),g&&g.options?g.update(h,i):(t.navigatorSeries=s.initSeries(h),s.setSortedData(),t.navigatorSeries.baseSeries=t,o.push(t.navigatorSeries))}),(d.data&&!(a&&a.length)||A(d))&&(e.hasNavigatorData=!1,(d=w(d)).forEach((t,i)=>{r.name="Navigator "+(o.length+1),(h=y(l.navigator.series,{color:s.series[i]&&!s.series[i].options.isInternal&&s.series[i].color||s.options.colors[i]||s.options.colors[0]},r,t)).data=t.data,h.data&&(e.hasNavigatorData=!0,o.push(s.initSeries(h)))})),t&&this.addBaseSeriesEvents()}addBaseSeriesEvents(){let t=this,i=t.baseSeries||[];i[0]&&i[0].xAxis&&i[0].eventsToUnbind.push(g(i[0].xAxis,"foundExtremes",this.modifyBaseAxisExtremes)),i.forEach(e=>{e.eventsToUnbind.push(g(e,"show",function(){this.navigatorSeries&&this.navigatorSeries.setVisible(!0,!1)})),e.eventsToUnbind.push(g(e,"hide",function(){this.navigatorSeries&&this.navigatorSeries.setVisible(!1,!1)})),!1!==this.navigatorOptions.adaptToUpdatedData&&e.xAxis&&e.eventsToUnbind.push(g(e,"updatedData",this.updatedDataHandler)),e.eventsToUnbind.push(g(e,"remove",function(){i&&v(i,e),this.navigatorSeries&&(v(t.series,this.navigatorSeries),x(this.navigatorSeries.options)&&this.navigatorSeries.remove(!1),delete this.navigatorSeries)}))})}getBaseSeriesMin(t){return this.baseSeries.reduce(function(t,i){return Math.min(t,i.xData&&i.xData.length?i.xData[0]:t)},t)}modifyNavigatorAxisExtremes(){let t=this.xAxis;if(void 0!==t.getExtremes){let i=this.getUnionExtremes(!0);i&&(i.dataMin!==t.min||i.dataMax!==t.max)&&(t.min=i.dataMin,t.max=i.dataMax)}}modifyBaseAxisExtremes(){let t,i;let e=this.chart.navigator,s=this.getExtremes(),a=s.min,r=s.max,o=s.dataMin,n=s.dataMax,h=r-a,l=e.stickToMin,d=e.stickToMax,c=k(this.ordinal?.convertOverscroll(this.options.overscroll),0),g=e.series&&e.series[0],p=!!this.setExtremes;!(this.eventArgs&&"rangeSelectorButton"===this.eventArgs.trigger)&&(l&&(t=(i=o)+h),d&&(t=n+c,l||(i=Math.max(o,t-h,e.getBaseSeriesMin(g&&g.xData?g.xData[0]:-Number.MAX_VALUE)))),p&&(l||d)&&S(i)&&(this.min=this.userMin=i,this.max=this.userMax=t)),e.stickToMin=e.stickToMax=null}updatedDataHandler(){let t=this.chart.navigator,i=this.navigatorSeries,e=t.reversedExtremes?0===Math.round(t.zoomedMin):Math.round(t.zoomedMax)>=Math.round(t.size);t.stickToMax=k(this.chart.options.navigator&&this.chart.options.navigator.stickToMax,e),t.stickToMin=t.shouldStickToMin(this,t),i&&!t.hasNavigatorData&&(i.options.pointStart=this.xData[0],i.setData(this.options.data,!1,null,!1))}shouldStickToMin(t,i){let e=i.getBaseSeriesMin(t.xData[0]),s=t.xAxis,a=s.max,r=s.min,o=s.options.range;return!!(S(a)&&S(r))&&(o&&a-e>0?a-e<o:r<=e)}addChartEvents(){this.eventsToUnbind||(this.eventsToUnbind=[]),this.eventsToUnbind.push(g(this.chart,"redraw",function(){let t=this.navigator,i=t&&(t.baseSeries&&t.baseSeries[0]&&t.baseSeries[0].xAxis||this.xAxis[0]);i&&t.render(i.min,i.max)}),g(this.chart,"getMargins",function(){let t=this.navigator,i=t.opposite?"plotTop":"marginBottom";this.inverted&&(i=t.opposite?"marginRight":"plotLeft"),this[i]=(this[i]||0)+(t.navigatorEnabled||!this.inverted?t.height+t.scrollbarHeight:0)+t.navigatorOptions.margin}),g(O,"setRange",function(t){this.chart.xAxis[0].setExtremes(t.min,t.max,t.redraw,t.animation,t.eventArguments)}))}destroy(){this.removeEvents(),this.xAxis&&(v(this.chart.xAxis,this.xAxis),v(this.chart.axes,this.xAxis)),this.yAxis&&(v(this.chart.yAxis,this.yAxis),v(this.chart.axes,this.yAxis)),(this.series||[]).forEach(t=>{t.destroy&&t.destroy()}),["series","xAxis","yAxis","shades","outline","scrollbarTrack","scrollbarRifles","scrollbarGroup","scrollbar","navigatorGroup","rendered"].forEach(t=>{this[t]&&this[t].destroy&&this[t].destroy(),this[t]=null}),[this.handles].forEach(t=>{m(t)}),this.navigatorEnabled=!1}}return O}),e(i,"Stock/Navigator/StandaloneNavigatorDefaults.js",[],function(){return{chart:{height:70,margin:[0,5,0,5]},exporting:{enabled:!1},legend:{enabled:!1},navigator:{enabled:!1},plotOptions:{series:{states:{hover:{enabled:!1}},marker:{enabled:!1}}},scrollbar:{enabled:!1},title:{text:""},tooltip:{enabled:!1},xAxis:{visible:!1},yAxis:{height:0,visible:!1}}}),e(i,"Stock/Navigator/StandaloneNavigator.js",[i["Core/Chart/Chart.js"],i["Stock/Navigator/Navigator.js"],i["Core/Globals.js"],i["Core/Utilities.js"],i["Core/Axis/Axis.js"],i["Stock/Navigator/StandaloneNavigatorDefaults.js"]],function(t,i,e,s,a,r){let{merge:o,addEvent:n,fireEvent:h,pick:l}=s;class d{static navigator(t,i){let s=new d(t,i);return e.navigators?e.navigators.push(s):e.navigators=[s],s}constructor(s,a){this.boundAxes=[],this.userOptions=a,this.chartOptions=o(e.getOptions(),r,{navigator:a});let n=new t(s,this.chartOptions);n.options=o(n.options,{navigator:{enabled:!0},scrollbar:{enabled:!0}}),this.chartOptions.navigator&&this.chartOptions.scrollbar&&(this.chartOptions.navigator.enabled=!0,this.chartOptions.scrollbar.enabled=!0),this.navigator=new i(n),n.navigator=this.navigator,this.initNavigator()}bind(i,e=!0){let s=this,r=i instanceof t?i.xAxis[0]:i;if(!(r instanceof a))return;let{min:o,max:h}=this.navigator.xAxis,l=[];if(e){let t=n(r,"setExtremes",t=>{("pan"===t.trigger||"zoom"===t.trigger||"mouseWheelZoom"===t.trigger)&&s.setRange(t.min,t.max,!0,"pan"!==t.trigger,{trigger:r})});l.push(t)}let d=n(this.navigator,"setRange",t=>{r.setExtremes(t.min,t.max,t.redraw,t.animation)});l.push(d);let c=this.boundAxes.filter(function(t){return t.axis===r})[0];c||(c={axis:r,callbacks:[]},this.boundAxes.push(c)),c.callbacks=l,r.series.forEach(t=>{t.options.showInNavigator&&s.addSeries(t.options)}),r.setExtremes(o,h),n(r,"destroy",t=>{t.keepEvents||this.unbind(r)})}unbind(t){if(!t){this.boundAxes.forEach(({callbacks:t})=>{t.forEach(t=>t())}),this.boundAxes.length=0;return}let i=t instanceof a?t:t.xAxis[0];for(let t=this.boundAxes.length-1;t>=0;t--)this.boundAxes[t].axis===i&&(this.boundAxes[t].callbacks.forEach(t=>t()),this.boundAxes.splice(t,1))}destroy(){this.boundAxes.forEach(({callbacks:t})=>{t.forEach(t=>t())}),this.boundAxes.length=0,this.navigator.destroy(),this.navigator.chart.destroy()}update(t,i){this.chartOptions=o(this.chartOptions,{navigator:t}),this.navigator.chart.update(this.chartOptions,i)}redraw(){this.navigator.chart.redraw()}addSeries(t){this.navigator.chart.addSeries(o(t,{showInNavigator:l(t.showInNavigator,!0)})),this.navigator.setBaseSeries()}initNavigator(){let t=this.navigator;t.top=1,t.xAxis.setScale(),t.yAxis.setScale(),t.xAxis.render(),t.yAxis.render(),t.series?.forEach(t=>{t.translate(),t.render(),t.redraw()});let{min:i,max:e}=this.getInitialExtremes();t.chart.xAxis[0].userMin=i,t.chart.xAxis[0].userMax=e,t.render(i,e)}getRange(){let{min:t,max:i}=this.navigator.chart.xAxis[0].getExtremes(),{userMin:e,userMax:s,min:a,max:r}=this.navigator.xAxis.getExtremes();return{min:l(t,a),max:l(i,r),dataMin:a,dataMax:r,userMin:e,userMax:s}}setRange(t,i,e,s,a){h(this.navigator,"setRange",{min:t,max:i,redraw:e,animation:s,eventArguments:o(a,{trigger:"navigator"})})}getInitialExtremes(){let{min:t,max:i}=this.navigator.xAxis.getExtremes();return{min:t,max:i}}}return d}),e(i,"masters/modules/navigator.src.js",[i["Core/Globals.js"],i["Stock/Navigator/StandaloneNavigator.js"],i["Stock/Navigator/NavigatorComposition.js"]],function(t,i,e){return t.StandaloneNavigator=t.StandaloneNavigator||i,t.navigator=t.StandaloneNavigator.navigator,e.compose(t.Chart,t.Axis,t.Series),t})});