window.onload = function() {
  console.log("onload");
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js', {scope: '/'})
      .then(function(reg) {
        console.log('登録に成功しました。 Scope は ' + reg.scope);
      }).catch(function(error) {
        console.log('登録に失敗しました。' + error);
      });
  }
}
