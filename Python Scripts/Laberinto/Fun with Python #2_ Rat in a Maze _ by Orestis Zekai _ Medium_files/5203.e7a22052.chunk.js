(self.webpackChunklite=self.webpackChunklite||[]).push([[5203],{65368:(e,n,i)=>{"use strict";i.d(n,{D:()=>u});var a=i(87329),t=i(88398),d={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"CatalogAddToListItem_catalog"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Catalog"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"Field",name:{kind:"Name",value:"visibility"}},{kind:"Field",name:{kind:"Name",value:"predefined"}},{kind:"Field",name:{kind:"Name",value:"version"}},{kind:"FragmentSpread",name:{kind:"Name",value:"WithToggleInsideCatalog_catalog"}}]}}].concat((0,a.Z)(t.s.definitions))},l={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"CatalogAddToList_catalog"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Catalog"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"CatalogAddToListItem_catalog"}}]}}].concat((0,a.Z)(d.definitions))},o=i(97147),m={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"YourCatalogs_catalog"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Catalog"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"CatalogsListItem_catalog"}}]}}].concat((0,a.Z)(o.c.definitions))},r={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"GetCatalogsByUserReadingList_catalog"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Catalog"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"CatalogAddToList_catalog"},directives:[{kind:"Directive",name:{kind:"Name",value:"skip"},arguments:[{kind:"Argument",name:{kind:"Name",value:"if"},value:{kind:"Variable",name:{kind:"Name",value:"withCatalogDetails"}}}]}]},{kind:"FragmentSpread",name:{kind:"Name",value:"YourCatalogs_catalog"},directives:[{kind:"Directive",name:{kind:"Name",value:"include"},arguments:[{kind:"Argument",name:{kind:"Name",value:"if"},value:{kind:"Variable",name:{kind:"Name",value:"withCatalogDetails"}}}]}]}]}}].concat((0,a.Z)(l.definitions),(0,a.Z)(m.definitions))},s={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"GetCatalogsByUserCatalogs_catalog"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Catalog"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"CatalogAddToList_catalog"},directives:[{kind:"Directive",name:{kind:"Name",value:"skip"},arguments:[{kind:"Argument",name:{kind:"Name",value:"if"},value:{kind:"Variable",name:{kind:"Name",value:"withCatalogDetails"}}}]}]},{kind:"FragmentSpread",name:{kind:"Name",value:"YourCatalogs_catalog"},directives:[{kind:"Directive",name:{kind:"Name",value:"include"},arguments:[{kind:"Argument",name:{kind:"Name",value:"if"},value:{kind:"Variable",name:{kind:"Name",value:"withCatalogDetails"}}}]}]}]}}].concat((0,a.Z)(l.definitions),(0,a.Z)(m.definitions))},u={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"query",name:{kind:"Name",value:"GetCatalogsByUserQuery"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"userId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"pagingOptions"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"CatalogPagingOptionsInput"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"type"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"CatalogType"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"withCatalogDetails"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Boolean"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",alias:{kind:"Name",value:"readingList"},name:{kind:"Name",value:"getPredefinedCatalog"},arguments:[{kind:"Argument",name:{kind:"Name",value:"userId"},value:{kind:"Variable",name:{kind:"Name",value:"userId"}}},{kind:"Argument",name:{kind:"Name",value:"type"},value:{kind:"EnumValue",value:"READING_LIST"}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"FragmentSpread",name:{kind:"Name",value:"GetCatalogsByUserReadingList_catalog"}}]}},{kind:"Field",name:{kind:"Name",value:"catalogsByUser"},arguments:[{kind:"Argument",name:{kind:"Name",value:"userId"},value:{kind:"Variable",name:{kind:"Name",value:"userId"}}},{kind:"Argument",name:{kind:"Name",value:"pagingOptions"},value:{kind:"Variable",name:{kind:"Name",value:"pagingOptions"}}},{kind:"Argument",name:{kind:"Name",value:"type"},value:{kind:"Variable",name:{kind:"Name",value:"type"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"catalogs"},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"GetCatalogsByUserCatalogs_catalog"}}]}},{kind:"Field",name:{kind:"Name",value:"paging"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"nextPageCursor"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}}]}}]}}]}}].concat((0,a.Z)(r.definitions),(0,a.Z)(s.definitions))}},88398:(e,n,i)=>{"use strict";i.d(n,{s:()=>a,m:()=>t});var a={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"WithToggleInsideCatalog_catalog"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Catalog"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"version"}},{kind:"Field",name:{kind:"Name",value:"predefined"}}]}}]},t={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"WithToggleInsideCatalog_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"viewerEdge"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"catalogsConnection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"catalogsContainingThis"},arguments:[{kind:"Argument",name:{kind:"Name",value:"type"},value:{kind:"EnumValue",value:"LISTS"}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"catalogId"}}]}},{kind:"Field",name:{kind:"Name",value:"predefinedContainingThis"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"predefined"}}]}}]}}]}}]}}]}},63508:(e,n,i)=>{"use strict";i.d(n,{a:()=>S});var a=i(34699),t=i(67294),d=i(19416),l=i(1109),o=i(85208),m=i(54758),r=i(13791),s=i(77355),u=i(40201),c=i(93310),k=i(31379),v=i(52069),g=i(87691),p=i(75221),N=i(78285),I=i(43487),f=i(50458);function S(e){var n=e.isVisible,i=e.hide,S=e.target,C=e.kind,y=e.viewer,F=t.useState(""),b=(0,a.Z)(F,2),T=b[0],D=b[1],_=t.useState(!1),h=(0,a.Z)(_,2),E=h[0],V=h[1],O=t.useState(""),w=(0,a.Z)(O,2),A=w[0],L=w[1],x=t.useState(!1),P=(0,a.Z)(x,2),j=P[0],R=P[1],Z=(0,I.v9)((function(e){return e.config.authDomain})),B=(0,o.Ax)(y.id),G=B.createCatalog,U=B.loading,Q=B.data,H=B.error,M=(0,m.T2)(),Y=(0,N.w)();t.useEffect((function(){if("Catalog"===(null==Q?void 0:Q.createCatalog.__typename))if(C&&S){var e=Q.createCatalog,n=e.id,i=e.version;M({userId:y.id,catalogId:n,version:i,kind:C,itemId:S.id}),z()}else window.location.assign((0,f.yk)(Q.createCatalog,Z))}),[null==Q?void 0:Q.createCatalog,C,null==S?void 0:S.id,M,y.id]),t.useEffect((function(){H&&Y({toastStyle:"RETRYABLE_ERROR",duration:4e3})}),[H,Y]);var W=t.useCallback((function(e){D(e.target.value)}),[D]),q=t.useCallback((function(e){L(e.target.value)}),[L]),z=t.useCallback((function(){D(""),L(""),V(!1),R(!1),i()}),[i]),X=t.useCallback((function(){var e=T.trim();e.length>0&&G({attributes:{title:e,description:A.trim(),type:p.HQ.LISTS,visibility:j?p.n2.PRIVATE:p.n2.PUBLIC}})}),[T,A,j,G]);return t.createElement(r.v,{isVisible:n,hide:z,confirmText:t.createElement(d.I,{loading:U,text:"Create"}),isDestructiveAction:!1,onConfirm:X,disableConfirm:!T.trim()||U||(0,l.G6)(T)||(0,l.z6)(A),hideOnConfirm:!1},t.createElement(s.x,{height:"400px"},t.createElement(s.x,{paddingBottom:"60px"},t.createElement(v.Dx,{scale:"L"},"Create new list")),t.createElement(s.x,{textAlign:"left",width:"400px",sm:{width:"100%"}},t.createElement(s.x,{paddingBottom:"20px"},t.createElement(u.n,{value:T,onChange:W,placeholder:"Give it a name",characterCountLimit:l.lp})),t.createElement(s.x,{paddingBottom:"20px"},E?t.createElement(s.x,{maxHeight:"170px",overflow:"auto"},t.createElement(u.n,{value:A,onChange:q,placeholder:"Description",isMultiline:!0,autoFocus:!0,characterCountLimit:l.B0})):t.createElement(c.r,{onClick:function(){return V(!0)}},t.createElement(g.F,{scale:"L",color:"ACCENT"},"Add a description"))),t.createElement(s.x,null,t.createElement(k.X,{checked:j,onChange:function(){return R(!j)},textScale:"L"},"Make it private")))))}},33974:(e,n,i)=>{"use strict";i.d(n,{S:()=>a,I:()=>t});var a={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"editCatalogItemsMutation_postViewerEdge"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"PostViewerEdge"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"catalogsConnection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"catalogsContainingThis"},arguments:[{kind:"Argument",name:{kind:"Name",value:"type"},value:{kind:"EnumValue",value:"LISTS"}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"catalogId"}},{kind:"Field",name:{kind:"Name",value:"version"}},{kind:"Field",name:{kind:"Name",value:"catalogItemIds"}}]}},{kind:"Field",name:{kind:"Name",value:"predefinedContainingThis"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"catalogId"}},{kind:"Field",name:{kind:"Name",value:"predefined"}},{kind:"Field",name:{kind:"Name",value:"version"}},{kind:"Field",name:{kind:"Name",value:"catalogItemIds"}}]}}]}}]}}]},t={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"mutation",name:{kind:"Name",value:"EditCatalogItems"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"catalogId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"String"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"version"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"String"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"operations"}},type:{kind:"NonNullType",type:{kind:"ListType",type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"CatalogItemMutateOperationInput"}}}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"editCatalogItems"},arguments:[{kind:"Argument",name:{kind:"Name",value:"catalogId"},value:{kind:"Variable",name:{kind:"Name",value:"catalogId"}}},{kind:"Argument",name:{kind:"Name",value:"version"},value:{kind:"Variable",name:{kind:"Name",value:"version"}}},{kind:"Argument",name:{kind:"Name",value:"operations"},value:{kind:"Variable",name:{kind:"Name",value:"operations"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"InlineFragment",typeCondition:{kind:"NamedType",name:{kind:"Name",value:"EditCatalogItemsSuccess"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"version"}},{kind:"Field",name:{kind:"Name",value:"operations"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"preprend"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"catalogItemId"}}]}},{kind:"Field",name:{kind:"Name",value:"append"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"catalogItemId"}}]}},{kind:"Field",name:{kind:"Name",value:"move"}}]}}]}}]}}]}}]}},54758:(e,n,i)=>{"use strict";i.d(n,{PH:()=>p,xt:()=>N,T2:()=>I,qY:()=>f,Yi:()=>S,oj:()=>y});var a=i(96156),t=i(34699),d=i(50361),l=i.n(d),o=i(21919),m=i(67294),r=i(12476),s=i(18627),u=i(75221),c=i(11462),k=i(33974);function v(e,n){var i=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);n&&(a=a.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),i.push.apply(i,a)}return i}function g(e){for(var n=1;n<arguments.length;n++){var i=null!=arguments[n]?arguments[n]:{};n%2?v(Object(i),!0).forEach((function(n){(0,a.Z)(e,n,i[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(i)):v(Object(i)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(i,n))}))}return e}var p="temp-cat-item-id",N="temp-cat-version";function I(){var e=(0,s.A)(),n=(0,m.useRef)(),i=(0,m.useRef)((function(i){var a=n.current;a&&"EditCatalogItemsSuccess"===i.editCatalogItems.__typename&&a.kind===u.ej.POST&&e.event("post.addToList",{listId:a.catalogId,postId:a.itemId})})).current,a=(0,o.D)(k.I,{onCompleted:i}),d=(0,t.Z)(a,1)[0];return(0,m.useCallback)((function(e){n.current=e,d({variables:{catalogId:e.catalogId,version:e.version,operations:[{preprend:{type:e.kind,id:e.itemId}}]},update:function(n,i){C({viewerId:e.userId,cache:n,result:i,catalogId:e.catalogId,itemId:e.itemId,kind:e.kind,operation:"preprend",predefined:e.predefined}),(0,r.p9)(n,e.userId,u.HQ.LISTS,e.catalogId)}})}),[d])}function f(e,n,i,a,t,d){var l=(0,s.A)();return(0,o.D)(k.I,{variables:{catalogId:n,version:i,operations:[{preprend:{type:t,id:a}}]},update:function(i,l){C({viewerId:e,cache:i,result:l,catalogId:n,itemId:a,kind:t,operation:"preprend",predefined:d}),d||(0,r.p9)(i,e,u.HQ.LISTS,n),(0,r.Rx)(i,n,[a],t)},optimisticResponse:{editCatalogItems:{__typename:"EditCatalogItemsSuccess",operations:[{__typename:"EditCatalogItemMutationOperationResponse",preprend:{__typename:"CatalogItemV2",catalogItemId:p},append:null,move:null}],version:N}},onCompleted:function(e){"EditCatalogItemsSuccess"===e.editCatalogItems.__typename&&t===u.ej.POST&&l.event("post.addToList",{listId:n,postId:a})}})}var S=function(e,n,i,a,t,d){var l=(0,s.A)(),m=a.map((function(e){return e.catalogItemIds})).flat();return(0,o.D)(k.I,{variables:{catalogId:n,version:i,operations:m.map((function(e){return{delete:{itemId:e}}}))},update:function(i,d){a.forEach((function(a){C({viewerId:e,cache:i,result:d,catalogId:n,itemId:a.entityId,kind:a.entityType,operation:"delete",predefined:t,deletedCatalogItemIds:a.catalogItemIds})})),(0,r.S_)(i,n,m,u.ej.POST),t||(0,r.p9)(i,e,u.HQ.LISTS,n)},optimisticResponse:{editCatalogItems:{__typename:"EditCatalogItemsSuccess",operations:a.map((function(e){return{__typename:"EditCatalogItemMutationOperationResponse",append:null,preprend:null,move:null}})),version:N}},onCompleted:function(e){if("EditCatalogItemsSuccess"===(null==e?void 0:e.editCatalogItems.__typename)){d&&d();var i=a.length;i>1?l.event("list.itemsDeleted",{listId:n,itemsCount:i}):a[0].entityType===u.ej.POST&&l.event("post.removeFromList",{listId:n,postId:a[0].entityId})}}})};function C(e){var n,i,t,d=e.cache,o=e.result,m=e.catalogId,s=e.viewerId,v=e.itemId,p=e.kind,N=e.operation,I=e.predefined,f=e.deletedCatalogItemIds,S=null===(n=o.data)||void 0===n?void 0:n.editCatalogItems;if("EditCatalogItemsSuccess"===(null==S?void 0:S.__typename)&&((0,r.UV)(d,m,S.version),p===u.ej.POST)){i=(0,c.Q)(v,s),"PostViewerEdge",t=k.S;var C="".concat("PostViewerEdge",":").concat(i),y=d.readFragment({id:C,fragment:t});if(null!=y&&y.catalogsConnection){var F=S.operations,b=S.version,T=F[0];if(!T||"move"===N)return;var D=l()(I?y.catalogsConnection.predefinedContainingThis:y.catalogsConnection.catalogsContainingThis),_=D.findIndex((function(e){return I?e.predefined===I:e.catalogId===m}));if("append"===N||"preprend"===N){var h=T[N];if(-1!==_)D[_].catalogItemIds.push(h.catalogItemId);else{var E={catalogId:m,version:b,catalogItemIds:[h.catalogItemId]};I&&(E.predefined=I),D.push(E)}}else if("delete"===N&&-1!==_&&f){var V=D[_].catalogItemIds;D[_].catalogItemIds=V.filter((function(e){return!f.includes(e)})),0===D[_].catalogItemIds.length&&D.splice(_,1)}d.writeFragment({id:C,fragment:t,data:g(g({},y),{},{catalogsConnection:g(g({},null==y?void 0:y.catalogsConnection),{},(0,a.Z)({},I?"predefinedContainingThis":"catalogsContainingThis",D))})})}}}function y(e,n,i,a){return(0,o.D)(k.I,{variables:{catalogId:e,version:n,operations:i},update:function(n){(0,r.uA)(n,e)},onCompleted:a})}},11462:(e,n,i)=>{"use strict";function a(e,n){return"postId:".concat(e,"-viewerId:").concat(n)}i.d(n,{Q:()=>a})}}]);
//# sourceMappingURL=https://stats.medium.build/lite/sourcemaps/5203.e7a22052.chunk.js.map