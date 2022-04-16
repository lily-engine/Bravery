document.getElementById("twitter-share-button").onclick = function() {
    let text = document.getElementById("tweet-text").innerText;
    let message = "あなたの勉強の進捗は" + text + "％です！今日も楽しく勉強しよう！"
    let hashtags = "ぴよぴよエンジニア";
    let url = encodeURIComponent(location.href)
    window.open("https://twitter.com/share?text=" + message + "&hashtags=" + hashtags + "&url=" + url);
}