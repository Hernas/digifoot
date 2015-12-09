$( document ).ready(function() {
  var $players = $(".players"),
      $home = [$players.find(".home1"), $players.find(".home2")],
      $visitors = [$players.find(".visitors1"), $players.find(".visitors2")],
      scoreSign = [],
      players = "";

  for (var i = 0; i < 45; ++i) {
    scoreSign.push("<span class=\"rly\"></span>");
  }

  // Reset score
  $("#scorehome, #scorevisitors").html(scoreSign.join(""));

  var cplayers = null;

  players = {
    "home": ["mfts", "brtoszhernas"],
    "visitors": ["adasd", "232323"]
  }

  var scored = function() {
    var goals = {
      "home": 2,
      "visitors": 3
    };

    ["home", "visitors"].forEach(function(side) {
      $("#score" + side).attr("class", ["scorecard", ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][goals[side]] || "full"].join(" "));
    });

    $("#scoreboard .js_undo")[goals.home + goals.visitors > 0 ? "removeClass" : "addClass"]("hide js_disabled");

    if (cplayers == null || players != cplayers) {
      var l = players.home.length;
      if (l > 0) {
        for (var i = 0; i < l; ++i) {
          $home[i].text(players.home[i]);
          $visitors[i].text(players.visitors[i]);
        }
        if (l == 1) {
         $players.addClass("opponents2");
        } else {
         $players.removeClass("opponents2");
        }
        $(".players").addClass("show");
      } else {
        $(".players").removeClass("show");
      }
      players = cplayers;
    }
  };
  scored();
  return {};
});
