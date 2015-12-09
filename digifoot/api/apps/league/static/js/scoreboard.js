var scoreSign = [];
$(document).ready(function () {
  for (var i = 0; i < 45; ++i) {
    scoreSign.push("<span class=\"rly\"></span>");
  }
  // Reset score
  $("#scorehome, #scorevisitors").html(scoreSign.join(""));
});


var scored = function (white, black) {
  var goals = {
    "home": white,
    "visitors": black
  };

  ["home", "visitors"].forEach(function (side) {
    $("#score" + side).attr("class", ["scorecard", ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][goals[side]] || "full"].join(" "));
  });

  $("#scoreboard .js_undo")[goals.home + goals.visitors > 0 ? "removeClass" : "addClass"]("hide js_disabled");
};
