angular.module('hardcarryApp.champion', ['ngRoute'])

.controller('championCtrl', ["$routeParams", function($routeParams){
    this.id = $routeParams.id;
    this.data = {name: "Lee Sin",
                 key: "LeeSin",
                 nickname: "The Blind Monk",
                 numberOfSkins: 8,
                 attack: 8,
                 defense: 5,
                 difficulty: 6,
                 magic: 3,
                 allyTips: "Use Sonic Wave before Dragon's Rage so you can chase the target with Resonating Strike.",
                 enemyTips: "Stay spread out to minimize the impact of Lee Sin's ultimate, Dragon's Rage.",
                 parType: "Energy",
                 blurb: "As a young teen, Lee Sin was intent on becoming a summoner. His will and dedication were unmatched by any of his peers, and his skill drew the attention of Reginald Ashram, the League's High Councilor at the time. While studying at the Arcanum Majoris,...",
                 lore: "As a young teen, Lee Sin was intent on becoming a summoner. His will and dedication were unmatched by any of his peers, and his skill drew the attention of Reginald Ashram, the League's High Councilor at the time. While studying at the Arcanum Majoris, Lee Sin became frustrated with instruction paced for the other students. He spent his free time researching the nuances of summoning in hopes of graduating sooner. He made amazing advances in his arcane studies, surpassing all other students. By all indications, he would have become one of the League's greatest summoners were it not for one terrible mistake. Too impatient, he attempted to test his ability by summoning a beast from the Plague Jungles. What he summoned instead was a young boy, but not in one piece. He barely had time to look the boy in what was once his face before the jumbled human mass fell lifeless to the floor. A League investigation later revealed that the boy's entire village was obliterated by feedback from the ritual.<br><br>Lee Sin's talents were so promising that the League was willing to overlook the incident, but he could never forgive himself. He left the Institute and journeyed to the Shojin Monastery for eternal repentance, swearing never to practice magic again. Years later, hoping to atone for his crime with martyrdom, he set himself ablaze as a protest of the Noxian occupation of Ionia. He remained alive in this state, enduring searing agony for weeks. His actions paved the way for a League match wherein Ionia prevailed, but by the time he was doused, his eyes had been burned completely from their sockets. Hailed as a savior, he was reborn, and his will to act invigorated. He joined the League of Legends to continue his atonement with sweat and blood, a true monk's only possessions.<br><br>''The actions of one may sunder the world, but the efforts of many may rebuild it.''<br>- Lee Sin",
                 youtube: "https://www.youtube.com/embed/e6SleHuJjLo"
                };
}]);
