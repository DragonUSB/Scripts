(self.webpackChunklite=self.webpackChunklite||[]).push([[397],{51277:(e,n,i)=>{"use strict";i.d(n,{v:()=>l});var t=i(87329),a=i(48172),o=i(57477),d={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"OverflowMenuWithNegativeSignal_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"collection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"FragmentSpread",name:{kind:"Name",value:"OverflowMenuItemUndoClaps_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"AddToCatalogBase_post"}}]}}].concat((0,t.Z)(a.g.definitions),(0,t.Z)(o._C.definitions))},l={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"OverflowMenuButtonWithNegativeSignal_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"visibility"}},{kind:"FragmentSpread",name:{kind:"Name",value:"OverflowMenuWithNegativeSignal_post"}}]}}].concat((0,t.Z)(d.definitions))}},91743:(e,n,i)=>{"use strict";i.d(n,{t:()=>V});var t=i(67294),a=i(41802),o=i(6443),d=i(39727),l=i(66227),r=i(75221),s=i(22122),m=i(96156),c=i(34699),u=i(65331),k=i(17778),v=i(78038),p=i(38352),g=i(51066),S=i(77355),N=i(93310),f=i(73917),h=i(66411),F=i(77280),y=i(43487);function P(){return P=Object.assign?Object.assign.bind():function(e){for(var n=1;n<arguments.length;n++){var i=arguments[n];for(var t in i)Object.prototype.hasOwnProperty.call(i,t)&&(e[t]=i[t])}return e},P.apply(this,arguments)}var b=t.createElement("path",{d:"M6.2 16.8A7.5 7.5 0 1 0 16.8 6.2 7.5 7.5 0 0 0 6.2 16.8z",stroke:"#000",strokeWidth:2,strokeLinecap:"round"}),w=t.createElement("path",{d:"M6 6l11 11",stroke:"#000",strokeWidth:2});const C=function(e){return t.createElement("svg",P({width:19,height:19,viewBox:"0 0 23 23",fill:"none"},e),b,w)};var I=i(68894),O=i(87329),D=i(51615),_=i(59250),E=i(61095),T=i(18627),x=function(e){var n=e.creatorId,i=e.muteAuthor,a=e.hidePopover,o=e.eventData,d=e.isActiveExpandedPost,l=e.unfollowUser,r=(0,h.pK)(),s=(0,T.A)(),m={id:n||""},c=(0,E.Pd)(m).viewerEdge,u=!(null==c||!c.isFollowing),k=!(null==c||!c.isMuting),v=(0,D.k6)(),g=(0,_.jM)(),S=g.mutedAuthorIds,f=g.setMutedAuthorIds,F=g.isMutingFromHomeFeed,y=t.useCallback((function(e){f([].concat((0,O.Z)(S),[e]))}),[S]);return n?u?t.createElement(p.Sl,null,t.createElement(N.r,{onClick:function(){s.event("user.unfollowed",{targetUserId:n,source:r}),l(),a()}},"Unfollow this author")):k?null:t.createElement(p.Sl,null,t.createElement(N.r,{onClick:function(){s.event("user.muted",o),i(),F&&(y(n),d&&v.goBack()),a()}},"Mute this author")):null},M=i(24415),A=i(75150),Z=function(e){var n=e.collectionId,i=e.hidePopover,a=e.mutePub,o=e.eventData,l=e.isActiveExpandedPost,r=e.unfollowCollection,s=(0,T.A)(),m=(0,h.pK)(),c={id:n||""},u=(0,d.g)(c).viewerEdge,k=!(null==u||!u.isFollowing),v=!(null==u||!u.isMuting),g=(0,_.jM)(),S=g.mutedPubIds,f=g.setMutedPubIds,F=g.isMutingFromHomeFeed,y=(0,D.k6)(),P=t.useCallback((function(e){f([].concat((0,O.Z)(S),[e]))}),[S]);return n?k?t.createElement(p.Sl,null,t.createElement(N.r,{onClick:function(){s.event("collection.unfollowed",{collectionId:n,followSource:m}),r(),i()}},"Unfollow this publication")):v?null:t.createElement(p.Sl,null,t.createElement(N.r,{onClick:function(){s.event("collection.muted",o),a(),F&&(P(n),l&&y.goBack()),i()}},"Mute this publication")):null},j=i(42732);function B(e,n){var i=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);n&&(t=t.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),i.push.apply(i,t)}return i}function R(e){for(var n=1;n<arguments.length;n++){var i=null!=arguments[n]?arguments[n]:{};n%2?B(Object(i),!0).forEach((function(n){(0,m.Z)(e,n,i[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(i)):B(Object(i)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(i,n))}))}return e}var L=function(e){var n=e.post,i=e.creatorId,a=e.collectionId,o=e.isActiveExpandedPost,d=e.setDismissedPostId,l=e.isResponsive,m=e.hideNegativeSignalItem,P=e.popoverPositioningStrategy,b=e.hideAddToList,w=void 0===b||b,O=e.viewer,D=e.hideOnScroll,_=e.testId,E=n.id,T=(0,I.O)(!1),B=(0,c.Z)(T,4),L=B[0],V=B[2],U=B[3],H=null==O?void 0:O.id,W=(0,v.l)(i,a),K=W.muteAuthor,Q=W.mutePub,z=(0,k.l)(i,a),G=z.unfollowUser,q=z.unfollowCollection,J=(0,h.pK)(),X=(0,F.PM)(),Y=(0,y.v9)((function(e){return e.navigation.referrer})),$=(0,y.v9)((function(e){return e.navigation.currentLocation})),ee={postId:E,location:$,referrer:Y,source:J,referrerSource:X},ne=(0,j.c)({post:n,onShowLess:V,isActiveExpandedPost:o,collectionId:a,setDismissedPostId:d}).handleShowLess,ie={kind:r.ej.POST,target:n},te=(0,t.useCallback)((function(e){return t.createElement(p.mX,null,!m&&t.createElement(S.x,{borderBottom:"neutral.primary",paddingBottom:"4px",marginBottom:"4px"},t.createElement(p.Sl,null,t.createElement(N.r,{onClick:ne,"aria-label":"Show less like this"},t.createElement(S.x,{display:"flex",flexDirection:"row",alignItems:"center",borderBottom:void 0,ariaHidden:"true"},t.createElement(S.x,{marginRight:"4px"},t.createElement(C,null)),t.createElement(S.x,null,"Show less like this"))))),!w&&t.createElement(p.Sl,null,t.createElement(N.r,{"aria-controls":"aria-id","aria-expanded":"false",onClick:function(){V(),e()}},"Add to list")),t.createElement(A.T,{post:n,hidePopover:V}),t.createElement(x,{creatorId:i,muteAuthor:K,isActiveExpandedPost:o,hidePopover:V,eventData:R({targetUserId:i},ee),unfollowUser:G}),a&&t.createElement(Z,{collectionId:a,mutePub:Q,isActiveExpandedPost:o,hidePopover:V,eventData:R({collection:a},ee),unfollowCollection:q}),t.createElement(g.z,{postId:E,viewerId:H,targetUserId:i||"",shouldShowShortenedCopy:!0,hidePopover:V}))}),[]);return i?t.createElement(u.a,(0,s.Z)({},ie,{viewer:O}),(function(e){var n=e.onClick;return t.createElement(f.J,{isVisible:L,positioningStrategy:P,targetDistance:10,hide:V,popoverRenderFn:function(){return te(n)},hideOnScroll:D},t.createElement(M.c,{onClick:U,ariaLabel:"More options",isResponsive:l,tooltipText:"More",testId:_}))})):null},V=function(e){var n=e.post,i=e.isActiveExpandedPost,s=e.setDismissedPostId,m=e.isResponsive,c=e.hideNegativeSignalItem,u=e.popoverPositioningStrategy,k=e.hideAddToList,v=void 0===k||k,p=e.hideOnScroll,g=e.testId,S=n.creator,N=n.collection,f=n.visibility,h=(0,o.H)(),F=h.loading,y=h.value,P=(0,d.g)(N).viewerEdge,b=!F&&!!y,w=!(null==P||!P.isEditor),C=(null==y?void 0:y.id)===(null==S?void 0:S.id),I=v||f===r.Wn.UNLISTED;return S&&b?w||C?t.createElement(l.B,null,(function(e){var i=e.show;return t.createElement(a.Z,{post:n,showLoadingIndicator:i,isResponsive:m,popoverPositioningStrategy:u,hideAddToList:I,hideOnScroll:p,testId:g})})):t.createElement(L,{post:n,creatorId:S.id,collectionId:null==N?void 0:N.id,isActiveExpandedPost:i,setDismissedPostId:s,isResponsive:m,hideNegativeSignalItem:c,popoverPositioningStrategy:u,hideAddToList:I,viewer:y,hideOnScroll:p,testId:g}):null}},42732:(e,n,i)=>{"use strict";i.d(n,{c:()=>S});var t=i(87329),a=i(82492),o=i.n(a),d=i(26075),l=i(90386),r=i(67294),s=i(51615),m=i(59250),c=i(25550),u=i(18627),k=i(66411),v=i(78285),p=i(77280),g=i(43487),S=function(e){var n=e.post,i=e.onShowLess,a=e.isActiveExpandedPost,S=e.collectionId,N=e.setDismissedPostId,f=n.id,h=(0,c.r)().viewerId,F=(0,s.k6)(),y=(0,m.jM)(),P=y.setSeeLessPostIds,b=y.isMutingFromHomeFeed,w=(0,v.w)(),C=(0,d.x)().cache,I=(0,u.A)(),O=(0,k.pK)(),D=(0,p.PM)(),_=(0,g.v9)((function(e){return e.navigation.referrer})),E=(0,g.v9)((function(e){return e.navigation.currentLocation})),T=(0,r.useRef)(null),x=(0,r.useCallback)((function(){T.current=window.setTimeout((function(){I.event("post.see_less",{userId:h,collection:S,postId:f,location:E,referrer:_,source:O,referrerSource:D})}),3e3)}),[]),M=(0,r.useCallback)((function(){null!==T.current&&window.clearTimeout(T.current)}),[]),A=(0,r.useCallback)((function(){C.modify({id:C.identify((0,l.kQ)("ROOT_QUERY")),fields:{webRecommendedFeed:function(e,n){var i=n.readField;return o()({},e,{items:e.items.filter((function(e){return(null==e?void 0:e.post)&&i("id",e.post)!==f}))})},intentionalFeed:function(e,n){var i=n.readField;return o()({},e,{items:e.items.filter((function(e){return!("HomeFeedItem"===(null==e?void 0:e.__typename)&&null!=e&&e.post&&i("id",e.post)===f)}))})}}})}),[f]);return{handleShowLess:(0,r.useCallback)((function(){x(),A(),b&&(P((function(e){return[].concat((0,t.Z)(e),[f])})),a&&F.goBack(),null==N||N(f)),w({toastStyle:"USER_NEGATIVE_SIGNAL",extraParams:{onClickUndo:M}}),null==i||i()}),[])}}},86106:(e,n,i)=>{"use strict";i.d(n,{H:()=>v,C:()=>g});var t=i(22122),a=i(67294),o=i(93310),d=i(92780),l=i(66411),r=i(14646),s=i(42498),m={S:"2px 8px",M:"8px 16px"},c=function(){return{whiteSpace:"nowrap"}},u=function(){return{marginRight:arguments.length>0&&void 0!==arguments[0]?arguments[0]:"8px",border:"none",padding:"0",cursor:"pointer"}},k=function(e){return function(){return{padding:"".concat(m[e]),position:"relative"}}},v=function(e){return function(n){return{backgroundColor:"".concat(n.colorTokens.background.neutral.secondary.base),borderRadius:"100px",border:"1px solid ".concat(e?n.colorTokens.border.neutral.secondary.base:n.colorTokens.border.neutral.primary.base),transition:"background 300ms ease",":hover":{backgroundColor:"".concat(n.colorTokens.background.neutral.secondary.base)}}}},p=function(e){if(e)return{overflow:"hidden",textOverflow:"ellipsis"}},g=(0,a.forwardRef)((function(e,n){var i=e.topic,m=e.scale,g=void 0===m?"M":m,S=e.color,N=void 0===S?"DARKER":S,f=e.onClick,h=e.shouldTruncate,F=void 0!==h&&h,y=e.source,P=e.href,b=e.innerRef,w=e.includeBorder,C=e.marginRight,I=(0,r.I)(),O=(0,d.n)({name:"detail",scale:g,color:N}),D="Topic"===i.__typename?(0,s.fl)(i.name||""):(0,s.fl)(i.displayTitle||"");return a.createElement(l.cW,{source:y,extendSource:!0},a.createElement(o.r,(0,t.Z)({href:P},F&&{className:I({width:"100%"})},"M"===g&&{className:I(u(C))},{onClick:f,"aria-current":w?"page":void 0,ref:n}),a.createElement("div",{className:I([k(g),v(w),O,c,p(F)]),ref:b},D)))}))},17235:(e,n,i)=>{"use strict";i.d(n,{P:()=>r});var t=i(67294),a=i(57326),o=i(43487),d=i(50458),l=i(86106),r=(0,t.forwardRef)((function(e,n){var i=e.topic,r=e.scale,s=e.color,m=e.index,c=e.onClick,u=e.shouldTruncate,k=e.includeBorder,v=e.marginRight,p=(0,o.v9)((function(e){return e.config.authDomain})),g=(0,o.v9)((function(e){return e.config.topicToTagMappings})),S=function(e,n){return"Topic"===e.__typename?n[e.slug]?n[e.slug]:e.slug:e.id||""}(i,g),N=i.id||void 0,f=S?(0,d.Ih)(S,p):"#",h=(0,a.S)({index:m,tagSlug:S}),F=h.containerRef,y=h.handleClick,P=t.useCallback((function(){null==c||c(i.id),y()}),[i.id,c,y]);return t.createElement(l.C,{topic:i,source:{topicId:N,index:m},href:f,scale:r,color:s,shouldTruncate:u,onClick:P,innerRef:F,includeBorder:k,marginRight:v,ref:n})}))},57326:(e,n,i)=>{"use strict";i.d(n,{S:()=>u});var t=i(96156),a=i(67294),o=i(18627),d=i(66411),l=i(18122),r=i(77280),s=i(43487);function m(e,n){var i=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);n&&(t=t.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),i.push.apply(i,t)}return i}function c(e){for(var n=1;n<arguments.length;n++){var i=null!=arguments[n]?arguments[n]:{};n%2?m(Object(i),!0).forEach((function(n){(0,t.Z)(e,n,i[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(i)):m(Object(i)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(i,n))}))}return e}var u=function(e){var n=e.index,i=e.tagSlug,t=(0,o.A)(),m=(0,d.Lk)(),u=(0,r.PM)(),k=(0,s.v9)((function(e){return e.navigation.referrer})),v=(0,s.v9)((function(e){return e.navigation.currentLocation})),p=(0,d.f0)(c(c({},m),{},{index:n,topicId:i})),g={referrer:k||v,referrerSource:u},S=a.useCallback((function(){t.event("tag.clicked",{tagSlug:i},c(c({},g),{},{source:p}))}),[i,t,p,u,g]);return{containerRef:(0,l.g)({onPresentedFn:function(){t.event("tag.presented",{tagSlug:i,source:p},g)}}),handleClick:S}}},36299:(e,n,i)=>{"use strict";i.d(n,{J8:()=>u,Uw:()=>m,mW:()=>s});var t=i(87329),a=i(94078),o=i(79987),d={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"HighlighSegmentContext_paragraph"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Paragraph"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"ParagraphRefsMapContext_paragraph"}}]}}].concat((0,t.Z)(o.p.definitions))},l={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"ActiveSelectionContext_highlight"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Quote"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"SelectionMenu_highlight"}}]}}].concat((0,t.Z)([{kind:"FragmentDefinition",name:{kind:"Name",value:"SelectionMenu_highlight"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Quote"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"userId"}},{kind:"Field",name:{kind:"Name",value:"user"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"}}]}}]}}]))},r={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"ActiveSelectionContext_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"SelectionMenu_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"PostNewNoteCard_post"}}]}}].concat((0,t.Z)([{kind:"FragmentDefinition",name:{kind:"Name",value:"SelectionMenu_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"isPublished"}},{kind:"Field",name:{kind:"Name",value:"isLocked"}},{kind:"Field",name:{kind:"Name",value:"latestPublishedVersion"}},{kind:"Field",name:{kind:"Name",value:"visibility"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"allowNotes"}}]}}]}}]),(0,t.Z)([{kind:"FragmentDefinition",name:{kind:"Name",value:"PostNewNoteCard_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"latestPublishedVersion"}}]}}]))},s={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"InteractivePostBody_postPreview"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"extendedPreviewContent"},arguments:[{kind:"Argument",name:{kind:"Name",value:"truncationConfig"},value:{kind:"ObjectValue",fields:[{kind:"ObjectField",name:{kind:"Name",value:"previewParagraphsWordCountThreshold"},value:{kind:"IntValue",value:"400"}},{kind:"ObjectField",name:{kind:"Name",value:"minimumWordLengthForTruncation"},value:{kind:"IntValue",value:"150"}},{kind:"ObjectField",name:{kind:"Name",value:"truncateAtEndOfSentence"},value:{kind:"BooleanValue",value:!0}},{kind:"ObjectField",name:{kind:"Name",value:"showFullImageCaptions"},value:{kind:"BooleanValue",value:!0}},{kind:"ObjectField",name:{kind:"Name",value:"shortformPreviewParagraphsWordCountThreshold"},value:{kind:"IntValue",value:"30"}},{kind:"ObjectField",name:{kind:"Name",value:"shortformMinimumWordLengthForTruncation"},value:{kind:"IntValue",value:"30"}}]}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"bodyModel"},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"PostBody_bodyModel"}}]}},{kind:"Field",name:{kind:"Name",value:"isFullContent"}}]}}]}}].concat((0,t.Z)(a.Pk.definitions))},m={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"InteractivePostBody_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"content"},arguments:[{kind:"Argument",name:{kind:"Name",value:"postMeteringOptions"},value:{kind:"Variable",name:{kind:"Name",value:"postMeteringOptions"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"isLockedPreviewOnly"}},{kind:"Field",name:{kind:"Name",value:"bodyModel"},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"PostBody_bodyModel"}},{kind:"Field",name:{kind:"Name",value:"paragraphs"},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"HighlighSegmentContext_paragraph"}},{kind:"FragmentSpread",name:{kind:"Name",value:"NormalizeHighlights_paragraph"}}]}}]}}]}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"allowNotes"}},{kind:"FragmentSpread",name:{kind:"Name",value:"PostBody_creator"}}]}},{kind:"FragmentSpread",name:{kind:"Name",value:"ActiveSelectionContext_post"}}]}}].concat((0,t.Z)(a.Pk.definitions),(0,t.Z)(d.definitions),(0,t.Z)([{kind:"FragmentDefinition",name:{kind:"Name",value:"NormalizeHighlights_paragraph"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Paragraph"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"Field",name:{kind:"Name",value:"text"}}]}}]),(0,t.Z)(a.v.definitions),(0,t.Z)(r.definitions))},c={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"InteractivePostBody_quote"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Quote"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"ActiveSelectionContext_highlight"}},{kind:"FragmentSpread",name:{kind:"Name",value:"HighlighSegmentContext_highlight"}},{kind:"FragmentSpread",name:{kind:"Name",value:"NormalizeHighlights_highlight"}},{kind:"FragmentSpread",name:{kind:"Name",value:"PostBody_highlight"}}]}}].concat((0,t.Z)(l.definitions),(0,t.Z)([{kind:"FragmentDefinition",name:{kind:"Name",value:"HighlighSegmentContext_highlight"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Quote"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"endOffset"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"paragraphs"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"}}]}},{kind:"Field",name:{kind:"Name",value:"startOffset"}},{kind:"Field",name:{kind:"Name",value:"userId"}}]}}]),(0,t.Z)([{kind:"FragmentDefinition",name:{kind:"Name",value:"NormalizeHighlights_highlight"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Quote"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"endOffset"}},{kind:"Field",name:{kind:"Name",value:"startOffset"}},{kind:"Field",name:{kind:"Name",value:"paragraphs"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"Field",name:{kind:"Name",value:"text"}}]}}]}}]),(0,t.Z)(a.XV.definitions))},u={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"query",name:{kind:"Name",value:"InteractivePostBodyQuery"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"postId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"showNotes"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Boolean"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"post"},arguments:[{kind:"Argument",name:{kind:"Name",value:"id"},value:{kind:"Variable",name:{kind:"Name",value:"postId"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"highlights"},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"InteractivePostBody_quote"}}]}},{kind:"Field",name:{kind:"Name",value:"privateNotes"},directives:[{kind:"Directive",name:{kind:"Name",value:"include"},arguments:[{kind:"Argument",name:{kind:"Name",value:"if"},value:{kind:"Variable",name:{kind:"Name",value:"showNotes"}}}]}],selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"PostBody_privateNote"}}]}}]}}]}}].concat((0,t.Z)(c.definitions),(0,t.Z)(a.w6.definitions))}},23515:(e,n,i)=>{"use strict";i.d(n,{S:()=>o});var t=i(87329),a=i(84130),o={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"PostPageBookmarkButton_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"AddToCatalogBookmarkButton_post"}}]}}].concat((0,t.Z)(a.G.definitions))}},31228:(e,n,i)=>{"use strict";i.d(n,{R:()=>r});var t=i(87329),a=i(10654),o=i(8045),d=i(51277),l=i(23515),r={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"PostFooterActionsBar_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"visibility"}},{kind:"Field",name:{kind:"Name",value:"allowResponses"}},{kind:"Field",name:{kind:"Name",value:"postResponses"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"count"}}]}},{kind:"Field",name:{kind:"Name",value:"isLimitedState"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"collection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"FragmentSpread",name:{kind:"Name",value:"MultiVote_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"PostSharePopover_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"OverflowMenuButtonWithNegativeSignal_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"PostPageBookmarkButton_post"}}]}}].concat((0,t.Z)(a.x.definitions),(0,t.Z)(o.G.definitions),(0,t.Z)(d.v.definitions),(0,t.Z)(l.S.definitions))}},8045:(e,n,i)=>{"use strict";i.d(n,{G:()=>r});var t=i(87329),a=i(4088),o=i(98007),d=i(97282),l={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"FriendLink_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"SusiClickable_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"useCopyFriendLink_post"}}]}}].concat((0,t.Z)(o.qU.definitions),(0,t.Z)(d.N.definitions))},r={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"PostSharePopover_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"mediumUrl"}},{kind:"Field",name:{kind:"Name",value:"title"}},{kind:"Field",name:{kind:"Name",value:"isPublished"}},{kind:"Field",name:{kind:"Name",value:"isLocked"}},{kind:"FragmentSpread",name:{kind:"Name",value:"usePostUrl_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"FriendLink_post"}}]}}].concat((0,t.Z)(a.u.definitions),(0,t.Z)(l.definitions))}},97282:(e,n,i)=>{"use strict";i.d(n,{N:()=>o,I:()=>d});var t=i(87329),a=i(4088),o={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"useCopyFriendLink_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"usePostUrl_post"}}]}}].concat((0,t.Z)(a.u.definitions))},d={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"mutation",name:{kind:"Name",value:"CreatePostShareKeyMutation"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"postId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"createPostShareKey"},arguments:[{kind:"Argument",name:{kind:"Name",value:"postId"},value:{kind:"Variable",name:{kind:"Name",value:"postId"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"InlineFragment",typeCondition:{kind:"NamedType",name:{kind:"Name",value:"PostShareKey"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"key"}}]}}]}}]}}]}}}]);
//# sourceMappingURL=https://stats.medium.build/lite/sourcemaps/397.2e086ee7.chunk.js.map