/* global conventions:
  1) everything is 1-indexed;
  2) output strings are in the same case as input strings.
*/
var ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var AUXCHARS = ",./<>?;':[]{}-=_+!@#$%^&*()_`~ " + '"';

function alph() { return ALPHABET; }
function author() { return "Michael Tang"; }

function contains(s, ch)
{
  s += ""; ch += "";
  return (s.indexOf(ch) > -1);
}

function remove_aux_chars(s)
{
  s += "";
  var ans = "";
  for (var i=0; i<s.length; i++)
  {
    var ch = s.charAt(i);
    if (!contains(AUXCHARS,ch))
      ans += ch;
  }
  return ans.toString();
}

function length(s)
{
  return remove_aux_chars(s).length;
}

function rev_alphanum(s) { ans=ALPHABET.search(s.toUpperCase()); if (ans>-1) return ans+1; else return ""; }

function index_into(s, i)
{
  s += ""; i += 0;
  return remove_aux_chars(s+"").charAt(i-1); // 1-indexing
}

function alphanum(i) { return index_into_alphabet(i); } // alias
function index_into_alphabet(i)
{
  i += 0;
  return index_into(ALPHABET,i);
}

function compare_strings(s1, s2)
{
  s1 += ""; s2 += "";
  var ans = "";
  for (var i=0; i<s1.length && i<s2.length; i++)
  {
    if (s1.charAt(i).toUpperCase() == s2.charAt(i).toUpperCase())
      ans += s1.charAt(i);
  }
  return ans;
}

function atbash(s)
{
  s += "";
  var ans = "";
  for (var i=0; i<s.length; i++)
  {
    var ch = s.charAt(i);
    if (contains(ALPHABET,ch.toUpperCase()))
    {
      var new_ch = ALPHABET.charAt(25-ALPHABET.indexOf(ch.toUpperCase()));
      if (contains(ALPHABET,ch))
        ans += new_ch;
      else { ans += new_ch.toLowerCase(); } 
    }
    else ans += ch;
  }
  return ans;
}

function caesar(s, n) 
{
  if (s.map) { return s.map(caesar); }
  
  s += ""; n += 0;
  var ans = "";
  for (var i=0; i<s.length; i++)
  {
    var ch = s.charAt(i);
    if (contains(ALPHABET,ch.toUpperCase()))
    {
      var new_ch = ALPHABET.charAt(
        (((ALPHABET.indexOf(ch.toUpperCase())+n)%26)+26)%26); // ensures % gives a positive number
      if (contains(ALPHABET,ch))
        ans += new_ch;
      else { ans += new_ch.toLowerCase(); } 
    }
    else ans += ch;
  }
  return ans;
} 

function reverse(s)
{
  s += "";
  var ans = "";
  for (var i=s.length-1; i>=0; i--)
    ans += s.charAt(i);
  return ans;
}