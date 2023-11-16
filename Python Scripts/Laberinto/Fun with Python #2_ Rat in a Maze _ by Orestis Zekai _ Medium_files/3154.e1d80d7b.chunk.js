(self.webpackChunklite=self.webpackChunklite||[]).push([[3154],{20197:(e,n,t)=>{"use strict";t.d(n,{z:()=>i});var i={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"mutation",name:{kind:"Name",value:"UserBlockMutation"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"targetUserId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"userId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"blockUser"},arguments:[{kind:"Argument",name:{kind:"Name",value:"userId"},value:{kind:"Variable",name:{kind:"Name",value:"userId"}}},{kind:"Argument",name:{kind:"Name",value:"targetUserId"},value:{kind:"Variable",name:{kind:"Name",value:"targetUserId"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"viewerEdge"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"isBlocking"}}]}}]}}]}}]}},88776:(e,n,t)=>{"use strict";t.d(n,{E:()=>i});var i={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"mutation",name:{kind:"Name",value:"UserUnblockMutation"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"targetUserId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"userId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"unblockUser"},arguments:[{kind:"Argument",name:{kind:"Name",value:"userId"},value:{kind:"Variable",name:{kind:"Name",value:"userId"}}},{kind:"Argument",name:{kind:"Name",value:"targetUserId"},value:{kind:"Variable",name:{kind:"Name",value:"targetUserId"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"viewerEdge"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"isBlocking"}}]}}]}}]}}]}},66021:(e,n,t)=>{"use strict";t.d(n,{q:()=>b});var i=t(96156),a=t(67294),r=t(78038),l=t(6443),o=t(39727),d=t(61095),u=t(38352),c=t(93310),m=t(18627),s=t(66411),k=t(77280),p=t(43487);function v(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);n&&(i=i.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,i)}return t}function f(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?v(Object(t),!0).forEach((function(n){(0,i.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):v(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var g=function(){return null},b=function(e){var n=e.hidePopover,t=void 0===n?g:n,i=e.creator,v=e.collection,b=e.postId,h=e.setIsAuthorOrPubMuted,y=e.setMutedAuthorId,N=e.setMutedPubId,I=e.isMutingFromHomeFeed,E=(i||{}).id,U=(0,d.Pd)(i).viewerEdge,S=!(null==U||!U.isMuting),B=null==v?void 0:v.id,w=(0,o.g)(v).viewerEdge,O=null==w?void 0:w.isMuting,C=(0,l.H)().value,V=i&&C&&E===C.id,_=(0,r.l)(E,B),D=_.muteAuthor,F=_.unmuteAuthor,T=_.mutePub,A=_.unmutePub,P=(0,m.A)(),R=(0,s.pK)(),x=(0,k.PM)(),M=(0,p.v9)((function(e){return e.navigation.referrer})),j={postId:b,location:(0,p.v9)((function(e){return e.navigation.currentLocation})),referrer:M,source:R,referrerSource:x};return a.createElement(a.Fragment,null,!!i&&!V&&a.createElement(u.Sl,{key:"author-mute-popover-item-".concat(b)},a.createElement(c.r,{linkStyle:"SUBTLE",onClick:function(){var e=S?"user.unmuted":"user.muted",n=f({targetUserId:E},j);P.event(e,n),S?F():D(),h&&h(!0),I&&y&&y(E),t()}},S?"Unmute this author":"Mute this author")),!!v&&!(null!=w&&w.isEditor)&&a.createElement(u.Sl,{key:"pub-mute-popover-item-".concat(b)},a.createElement(c.r,{linkStyle:"SUBTLE",onClick:function(){var e=O?"collection.unmuted":"collection.muted",n=f({collectionId:B},j);P.event(e,n),O?A():T(),h&&h(!0),I&&N&&N(B),t()}},O?"Unmute this publication":"Mute this publication")))}},96086:(e,n,t)=>{"use strict";t.d(n,{r:()=>o});var i=t(67294),a=t(1383),r=t(77355),l=t(93310);function o(e){var n=e.onConfirm,t=e.isVisible,o=e.hide,d=e.isInResponsesSidebar;return i.createElement(a.Q,{onConfirm:n,isVisible:t,hide:o,titleText:"Block this user?",confirmText:"Block",noPortal:d,withCloseButton:!d&&void 0,isDestructiveAction:!0,isResponse:d},i.createElement(r.x,{paddingBottom:"2px"},"They will no longer be able to follow you or view your content."),i.createElement(l.r,{inline:!0,linkStyle:"OBVIOUS",target:"_blank",href:"https://help.medium.com/hc/en-us/articles/217048077-Block-a-user"},"Learn more about blocking"),".")}},96462:(e,n,t)=>{"use strict";t.d(n,{F:()=>g});var i=t(34699),a=t(67294),r=t(32493),l=t(86706),o=t(78285),d=t(20197),u=(0,l.$j)()((function(e){var n=e.children,t=e.dispatch,i=e.targetUserId,l=e.viewerId,u=e.onCompleted;return a.createElement(r.m,{mutation:d.z,onCompleted:function(){t((0,o.Dx)({message:"Successfully blocked user."})),u&&u()},variables:{targetUserId:i,userId:l},optimisticResponse:{__typename:"Mutation",blockUser:{__typename:"User",id:i,viewerEdge:{__typename:"UserViewerEdge",id:"userId:".concat(i,"-viewerId:").concat(l),isBlocking:!0}}}},(function(e){return n({mutate:e})}))})),c=t(88776),m=(0,l.$j)()((function(e){var n=e.children,t=e.dispatch,i=e.targetUserId,l=e.viewerId,d=e.onCompleted;return a.createElement(r.m,{mutation:c.E,onCompleted:function(){t((0,o.Dx)({message:"Successfully unblocked user."})),d&&d()},variables:{targetUserId:i,userId:l},optimisticResponse:{__typename:"Mutation",unblockUser:{__typename:"User",id:i,viewerEdge:{__typename:"UserViewerEdge",id:"userId:".concat(i,"-viewerId:").concat(l),isBlocking:!1}}}},(function(e){return n({mutate:e})}))})),s=t(61095),k=t(38352),p=t(96086),v=t(93310),f=t(68894),g=function(e){var n=e.hidePopover,t=e.creator,r=e.viewer,l=(t||{}).id,o=(0,s.Pd)({id:l}).viewerEdge,d=!(null==o||!o.isBlocking),c=(0,f.O)(!1),g=(0,i.Z)(c,3),b=g[0],h=g[1],y=g[2],N=function(){y(),n()};return a.createElement(a.Fragment,null,d?null:a.createElement(u,{targetUserId:l,viewerId:r.id,onCompleted:N},(function(e){var n=e.mutate;return a.createElement(p.r,{onConfirm:n,isVisible:b,hide:N})})),a.createElement(k.Sl,null,d?a.createElement(m,{targetUserId:l,viewerId:r.id,onCompleted:n},(function(e){var n=e.mutate;return a.createElement(v.r,{onClick:function(){n()}},"Unblock this author")})):a.createElement(v.r,{onClick:function(){h()}},"Block this author")))}},48517:(e,n,t)=>{"use strict";t.d(n,{j:()=>C});var i=t(34699),a=t(67294),r=t(32493),l=t(86706),o=t(18627),d=t(78285),u={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"mutation",name:{kind:"Name",value:"reportUserLink"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"userId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"targetUserId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"alsoBlockUser"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Boolean"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"reportAndMaybeBlockUser"},arguments:[{kind:"Argument",name:{kind:"Name",value:"userId"},value:{kind:"Variable",name:{kind:"Name",value:"userId"}}},{kind:"Argument",name:{kind:"Name",value:"targetUserId"},value:{kind:"Variable",name:{kind:"Name",value:"targetUserId"}}},{kind:"Argument",name:{kind:"Name",value:"alsoBlockUser"},value:{kind:"Variable",name:{kind:"Name",value:"alsoBlockUser"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"viewerEdge"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"isBlocking"}}]}}]}}]}}]},c=(0,l.$j)()((function(e){var n=e.children,t=e.dispatch,i=e.targetUserId,l=e.viewerId,c=e.onOptimisticComplete,m=e.isBlocking,s=(0,o.A)();return a.createElement(r.m,{mutation:u,onCompleted:function(){t((0,d.Dx)({message:"Successfully reported user."}))}},(function(e){return n({mutate:function(n){var t=e({variables:{userId:l,targetUserId:i,alsoBlockUser:n},onCompleted:function(){s.event("author.flagged",{authorId:i})},optimisticResponse:{__typename:"Mutation",reportAndMaybeBlockUser:{__typename:"User",id:i,viewerEdge:{__typename:"UserViewerEdge",id:"userId:".concat(i,"-viewerId:").concat(l),isBlocking:m||n}}}});return c&&c(),t}})}))})),m=t(61095),s=t(38352),k=t(6610),p=t(5991),v=t(63349),f=t(10379),g=t(46070),b=t(77608),h=t(91583),y=t(77355),N=t(31379),I=t(47230),E=t(93310),U=t(20113),S=t(90586),B=t(87691);var w=function(e){(0,f.Z)(r,e);var n,t,i=(n=r,t=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}(),function(){var e,i=(0,b.Z)(n);if(t){var a=(0,b.Z)(this).constructor;e=Reflect.construct(i,arguments,a)}else e=i.apply(this,arguments);return(0,g.Z)(this,e)});function r(e){var n;(0,k.Z)(this,r),(n=i.call(this,e)).handleAlsoBlockUserChange=function(e){n.setState({alsoBlockUser:e.target.checked})},n.handleReportClick=function(){var e=n.state.alsoBlockUser;(0,n.props.onConfirm)(e)},n.handleAlsoBlockUserChange=n.handleAlsoBlockUserChange.bind((0,v.Z)(n)),n.handleReportClick=n.handleReportClick.bind((0,v.Z)(n));var t=e.withBlockOption;return n.state={alsoBlockUser:!!t},n}return(0,p.Z)(r,[{key:"render",value:function(){var e=this.props,n=e.isVisible,t=e.hide,i=e.withBlockOption,r=this.state.alsoBlockUser;return a.createElement(h.V,{isVisible:n,hide:t},a.createElement(U.X6,{scale:"L",tag:"h1"},"Report this user?"),a.createElement(y.x,{paddingTop:"8px",paddingBottom:"24px"},a.createElement(S.QE,{scale:"M"},"This will flag this user for review with our support team."),i?a.createElement(y.x,{paddingTop:"8px"},a.createElement(N.X,{checked:r,onChange:this.handleAlsoBlockUserChange},"Also block this user. They will no longer be able to follow you or view your content.")):null),a.createElement(I.zx,{buttonStyle:"OBVIOUS",onClick:this.handleReportClick},r?"Report and block":"Report"),a.createElement(y.x,{paddingLeft:"8px",display:"inline-block"},a.createElement(I.zx,{buttonStyle:"SUBTLE",onClick:t},"Cancel")),a.createElement(y.x,{paddingTop:"48px"},a.createElement(B.F,{scale:"M",tag:"div"},"Report"," ",a.createElement(E.r,{href:"https://medium.com/policy/mediums-copyright-and-dmca-policy-d126f73695",linkStyle:"OBVIOUS",inline:!0},"copyright infringement")," ","or"," ",a.createElement(E.r,{href:"https://medium.com/policy/mediums-trademark-policy-e3bb53df59a7",linkStyle:"OBVIOUS",inline:!0},"trademark infringement"),".",a.createElement("br",null),"Read"," ",a.createElement(E.r,{href:"https://medium.com/policy/medium-rules-30e5502c4eb4",linkStyle:"OBVIOUS",inline:!0},"our rules"),".")))}}]),r}(a.Component),O=t(68894),C=function(e){var n=e.hidePopover,t=e.creator,r=e.viewer,l=(t||{}).id,o=(0,m.Pd)(t).viewerEdge,d=!(null==o||!o.isBlocking),u=(0,O.O)(!1),k=(0,i.Z)(u,3),p=k[0],v=k[1],f=k[2],g=function(){f(),n()};return a.createElement(a.Fragment,null,a.createElement(c,{targetUserId:l,viewerId:r.id,isBlocking:d,onOptimisticComplete:g},(function(e){var n=e.mutate;return a.createElement(w,{onConfirm:n,isVisible:p,hide:g,withBlockOption:!d})})),a.createElement(s.Sl,null,a.createElement(E.r,{onClick:function(){v()}},"Report this author")))}}}]);
//# sourceMappingURL=https://stats.medium.build/lite/sourcemaps/3154.e1d80d7b.chunk.js.map