#!/usr/bin/perl
########################################################
#���v�ŧi
#�{���W�١GTMmany �u�W�ǰT
#�{�������G1.2.3
#�{���@�̡GTurtleMan
#�@�̹q�l�Gturtlemn@pchome.com.tw
#�S�O�����G
# ��l�X����W�ഫ�����ѦҦ� �������� ���E������ �ҳЧ@���uNSLOOKUP 1.00  ����W�٬d�ߵ{���v
# �t�~cookie�]�w�Ϊ���ƳB�z�ѦҦۨk�B�溸���uMale Nurse Guest�v�{��
#�H�W���v�ŧi�A�ФŧR��
################�]�w�}�l##################################
$datafile='many.txt';##������ƪ��ɮצ�}
$cycle=10;##�۰�reload���g��(���G��)
$bgcolor='FFFFFF';##�I���C��
$cgiurl='TMmany.cgi';##�D�{���ɦW
$usehtmlpass='~!12345!~';##(�ϥ�HTML���K�X)�`�N�G������7�ӥb�Φr���m�m���ӳ�޸����n�o�e�T���ɥ[�b�r��̫e���N�i�H�ϥ�html�y�k�F
$listcolor='0080C0';##�u�W�H�ƿ���r�C��
$listbgcolor='Ffffff';##�u�W�H�ƿ��I���C��
$cmdlistcolor='F0F8FF';##�t�ΩR�O����r�C��
$cmdlistbgcolor='0080C0';##�t�ΩR�O���I���C��
$onlistcolor='0080C0';##�u�W�H�W����r�C��
$onlistbgcolor='F0F8FF';##�u�W�H�W���I���C��
$nickcount=12;##�]�w�ʺ٥i��J���̦h�r����(���Φr�@�r��2�r��)
################�]�w����##################################
$version='1.2.3';
$now=time();
$ip=$ENV{'REMOTE_ADDR'};
$options="";
$found=0;
$count=0;
%FORM=&get_form;
#########################################################################
if($FORM{job} eq "setnick") { &setnick; }
elsif($FORM{job} eq "chgnick") { &chgnick; }
elsif($FORM{job} eq "wrtmsg") { &wrtmsg; }
elsif($FORM{job} eq "savemsg") { &savemsg; }
elsif($FORM{job} eq "show") { &show; }
elsif($FORM{job} eq "chgmsgonoff") { &chgmsgonoff; }
elsif($FORM{job} eq "readme") { &readme; }
else { &main; }
#########################################################################
sub main{
#########################################################################
open (FILE, $datafile);@DATAS=<FILE>;close (FILE);
open(FILE,">$datafile");
$mynick=$ip;
foreach $line (@DATAS)
{
 ($recip,$recadd,$recmsgonoff,$rectime,$recintime,$recnick,$recmsg)=split("��",$line);
 chop $recmsg;
 if(($now-$rectime)<=($cycle+30))
 {
  if($ip eq $recip)
  {
   $message=$recmsg;
   $found=1;
   $count++;
   print FILE "$recip��$recadd��$recmsgonoff��$now��$recintime��$recnick��\n";
   $options=$options."<OPTION VALUE=1 STYLE=background-color:$onlistbgcolor\;color:$onlistcolor>�� ";
   if($recnick ne "")
   {
    $options=$options.$recnick."\n";
    $mynick=$recnick;
   }
   else
   {
    $options=$options.$ip."\n";
   }
  }
  ## $ip ne $recip
  else
  {
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$recnick��$recmsg\n";
   if($recnick ne "")
   {
    $options=$options."<OPTION VALUE=$recip��$recnick STYLE=background-color:$onlistbgcolor\;color:$onlistcolor> �@ ";
    $options=$options.$recnick."\n";
   }
   else
   {
    $options=$options."<OPTION VALUE=$recip�� STYLE=background-color:$onlistbgcolor\;color:$onlistcolor> ";
    $options=$options.$recip."\n";
   }
   $count++;
  }
 }
}#End foreach
if(!$found)
{
 ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time);
 $mon++;
#------ip�ഫ
 $arg=$ip;
 if($arg =~ /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/)
 {
  @bytes = split (/\./,$arg);
  $pack = pack("C4", @bytes);
 }
 else
 {
  ($pack) = (gethostbyname($arg))[4];
 }
 ($name, $aliases, $addrtype, $length, @addrs) = gethostbyaddr($pack, 2);
 if($name eq "")
 {
  $arg=$ip;
 }
 else
 {
  $arg=$name;
 }
#------
 &get_cookie;
 print FILE "$ip��$arg��on��$now��$mon/$mday $hour:$min:$sec��$cookienick��\n";
 $options=$options."<OPTION VALUE=1 STYLE=background-color:$onlistbgcolor\;color:$onlistcolor>�� ";
 if($cookienick eq "")
 {
  $options=$options.$ip."\n";
 }
 else
 {
  $options=$options.$cookienick."\n";
 }
 $count++;
}
close(FILE);
#########################################################################
print "Content-type: text/html\n\n";
print "<HTML><HEAD><meta http-equiv=\"Content-Type\" content=\"text/html\; charset=big5\"><TITLE>TMmany</TITLE>\n";
print "<META HTTP-EQUIV=REFRESH CONTENT=\"$cycle;URL=$cgiurl\">\n";
print "<SCRIPT LANGUAGE=JavaScript>\n";
if($message ne "")
{
 print "message=window.open('','','menubar=no,status=no,toolbar=no,scrollbars=yes,width=300,height=300,left=300,top=200')\;\n";
 print "message.document.writeln('<HTML><HEAD><TITLE>����T��</TITLE></HEAD>')\;\n";
 print "message.document.writeln('<BODY BGCOLOR=$bgcolor STYLE=\"font-size:8pt\;font-family:�s�ө���,Arial\">')\;\n";
 print "message.document.writeln('<TABLE ALIGN=CENTER><TR><TD STYLE=position:relative\\;color:white\\;font-size:8pt\\;text-decoration:underline\\;letter-spacing:5px\\;filter:glow(color=red,strength=1)\\;>����T��</TD></TR></TABLE><BR>')\;\n";
 print "message.document.writeln('<CENTER><input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;></CENTER><HR>')\;\n";
 print "message.document.writeln('$message')\;\n";
 print "message.document.writeln('<HR><CENTER><input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;></CENTER>')\;\n";
 print "message.document.writeln('<DIV STYLE=color:blue\;font-size:8pt\;text-align:center\;padding-top:20px\;letter-spacing:2px>TMmany �u�W�ǰT v $version<BR>���s�ƪ��G<a href=http://222721.24cc.com target=_blank>��~�t�x�~~��</a><FONT COLOR=FF0000 STYLE=font-size:8pt>���H��E��~*</FONT></DIV></CENTER>')\;\n";
 print "message.document.writeln('</BODY></HTML>')\;\n";
}
print "function change(obj)\n";
print "{\n";
print " if(obj.options[obj.selectedIndex].value==0)\n";
print " {\n";
print "  location.replace(\'$cgiurl\')\;\n";
print " }\n";
print " else if(obj.options[obj.selectedIndex].value==1)\n";
print " {\n";
print "  obj.selectedIndex=0\;\n";
print "  window.open('$cgiurl?job=setnick','','menubar=no,status=no,toolbar=no,width=180,height=170,left=300,top=200')\;\n";
print " }\n";
print " else if(obj.options[obj.selectedIndex].value==2)\n";
print " {\n";
print "  obj.selectedIndex=0\;\n";
print "  window.open('$cgiurl?job=wrtmsg&sender=$mynick&towho=all���j�a','','menubar=no,status=no,toolbar=no,width=180,height=180,left=300,top=200')\;\n";
print " }\n";
print " else if(obj.options[obj.selectedIndex].value==3)\n";
print " {\n";
print "  obj.selectedIndex=0\;\n";
print "  window.open('$cgiurl?job=show','','menubar=no,scrollbars=yes,status=no,toolbar=no,width=400,height=300,left=200,top=150')\;\n";
print " }\n";
print " else if(obj.options[obj.selectedIndex].value==4)\n";
print " {\n";
print "  location.replace(\'$cgiurl?job=chgmsgonoff\')\;\n";
print " }\n";
print " else if(obj.options[obj.selectedIndex].value==5)\n";
print " {\n";
print "  obj.selectedIndex=0\;\n";
print "  window.open('$cgiurl?job=readme','','menubar=no,scrollbars=yes,status=no,toolbar=no,width=500,height=300,left=200,top=150')\;\n";
print " }\n";
print " else\n";
print " {\n";
print "  window.open('$cgiurl?job=wrtmsg&sender=$mynick&towho='+obj.options[obj.selectedIndex].value,'','menubar=no,status=no,toolbar=no,width=180,height=190,left=300,top=200')\;\n";
print "  obj.selectedIndex=0\;\n";
print " }\n";
print "}\n";
print "</SCRIPT>\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=$bgcolor topmargin=\"0\" leftmargin=\"0\"><CENTER>\n";
print "<FORM>\n";
print "<SELECT ONCHANGE='change(this)\;'>\n";
print "<OPTION SELECTED STYLE=background-color:$listbgcolor\;color:$listcolor>�b�u�H�ơG ".$count." </FONT>�H\n";
print $options;
print "<OPTION VALUE=0 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>�ššššššš�\n";
print "<OPTION VALUE=2 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>���ǰe�s���T����\n";
print "<OPTION VALUE=3 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>���Բӽu�W��ơ�\n";
print "<OPTION VALUE=4 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>���T�������}����\n";
print "<OPTION VALUE=5 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>���ϥλ����d�ҡ�\n";
print "<OPTION VALUE=0 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>���̷s�H�ƪ��p��\n";
print "<OPTION VALUE=0 STYLE=background-color:$cmdlistbgcolor\;color:$cmdlistcolor>�ááááááá�\n";
print "</SELECT>\n";
print "</FORM>\n";
#########################################################################
print "</CENTER></BODY></HTML>\n";
}#End of main
#########################################################################
sub setnick
{
 print "Content-type: text/html\n\n";
 print "<HTML><HEAD><meta http-equiv=\"Content-Type\" content=\"text/html\; charset=big5\"><TITLE>�ܧ�z���ʺ�</TITLE></HEAD>\n";
 print "<SCRIPT LANGUAGE=JavaScript>\n";
 print "function lengthcheck()\n";
 print "{\n";
 print " var total=0\;\n";
 print " for(i=0\;i<my.nick.value.length\;i++)\n";
 print " {\n";
 print "  if(my.nick.value.charCodeAt(i)>200)\n";
 print "   total+=2\;\n";
 print "  else\n";
 print "   total++\;\n";
 print " }\n";
 print " if(total>$nickcount)\n";
 print " {\n";
 print "  alert(\'��J�r��L���A�Э��s��J�I\')\;\n";
 print "  my.reset()\;\n";
 print "  my.nick.focus()\;\n";
 print "  return false\;\n";
 print " }\n";
 print " else if(total == 0)\n";
 print " {\n";
 print "  alert(\'�S����J����F��A�Э��s��J�I\')\;\n";
 print "  my.reset()\;\n";
 print "  my.nick.focus()\;\n";
 print "  return false\;\n";
 print " }\n";
 print " else\n";
 print "  return true\;\n";
 print "}\n";
 print "</SCRIPT>\n";
 print "<BODY BGCOLOR=$bgcolor ONLOAD=my.nick.focus()>\n";
 print "<FORM NAME=my ACTION=$cgiurl METHOD=post ONSUBMIT=return(lengthcheck())\;>\n";
 print "<TABLE ALIGN=CENTER CELLSPACING=3 STYLE=text-align:center\;font-size:8pt>\n";
 print "<TR><TD STYLE=position:relative\;color:white\;font-size:8pt\;text-decoration:underline\;letter-spacing:5px\;filter:glow(color=red,strength=1)\;>��J�ʺ�</TD><TR>\n";
 print "<TR><TD><INPUT TYPE=text NAME=nick SIZE=10 MAXLENGTH=12 STYLE=font-size:8pt\;color:green\;border-width:3px\;border-style:double\;border-color:darkcyan></TD></TR>\n";
 print "<TR><TD><INPUT TYPE=submit VALUE=�T�w STYLE=font-size:8pt\;color:brown\;background-color:powderblue\;border-width:1px\;border-style:solid\;border-color:darkcyan>\n";
 print "<INPUT TYPE=reset VALUE=�M�� STYLE=font-size:8pt\;color:brown\;background-color:powderblue\;border-width:1px\;border-style:solid\;border-color:darkcyan></TD></TR>\n";
 print "</TABLE>\n";
 print "<INPUT TYPE=hidden NAME=job VALUE=chgnick>\n";
 print "</FORM>\n";
 print "<HR><CENTER><input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;></CENTER>";
 print "</BODY></HTML>\n";
}
#########################################################################
sub chgnick
{
 $FORM{nick}=~s/��/||/g;
 open (FILE, $datafile);@DATAS=<FILE>;close (FILE);
 open(FILE,">$datafile");
 foreach $line (@DATAS)
 {
  ($recip,$recadd,$recmsgonoff,$rectime,$recintime,$recnick,$recmsg)=split("��",$line);
  chop $recmsg;
  if($ip eq $recip)
  {
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$FORM{nick}��$recmsg\n";
  }
  else
  {
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$recnick��$recmsg\n";
  }
 }
 close(FILE);
 &set_cookie;
 print "Content-type: text/html\n\n";
 print "<SCRIPT LANGUAGE=JavaScript>\n";
 print "window.close()\;\n";
 print "</SCRIPT>\n";
}
#########################################################################
sub wrtmsg
{
 @reciever=split(/��/,$FORM{towho});
 print "Content-type: text/html\n\n";
 print "<HTML><HEAD><meta http-equiv=\"Content-Type\" content=\"text/html\; charset=big5\"><TITLE>�ǰe�T��</TITLE>\n";
 print "<SCRIPT LANGUAGE=JavaScript>\n";
 print "\n";
 print "function codecheck()\n";
 print "{\n";
 print " if(my.msg.value.length == 0)\n";
 print " {\n";
 print "  alert(\'�S����J����F��A�Э��s��J�I\')\;\n";
 print "  my.msg.focus()\;\n";
 print "  return false\;\n";
 print " }\n";
 print " var result=1\;\n";
 print " var colors=0\;\n";
 print " var codes1=[\'~\!big\!~\',\'~\!/big\!~\',\'~\!small\!~\',\'~\!/small\!~\',\'~\!i\!~\',\'~\!/i\!~\',\'~\!b\!~\',\'~\!/b\!~\']\;\n";
 print " var codes2=[\'~\!red\!~\',\'~\!blue\!~\',\'~\!green\!~\',\'~\!purple\!~\',\'~\!dodgerblue\!~\',\'~\!deeppink\!~\',\'~\!lightgreen\!~\',\'~\!mediumpurple\!~\',\'~\!sienna\!~\',\'~\!olivedrab\!~\']\;\n";
 print " for(i=0\;i<codes1.length\;i+=2)\n";
 print " {\n";
 print "  if(codecount(codes1[i])!=codecount(codes1[i+1]))\n";
 print "   result=0\;\n";
 print " }\n";
 print " if(result)\n";
 print " {\n";
 print "  for(i=0\;i<codes2.length\;i++)\n";
 print "   colors+=codecount(codes2[i])\;\n";
 print "  if(colors!=codecount(\'~\!/color\!~\'))\n";
 print "   result=0\;\n";
 print " }\n";
 print " if(result)\n";
 print "  return true\;\n";
 print " else\n";
 print " {\n";
 print "  alert(\'�@�֢�ۢگS��r���ˬd���~�I\\n�@�ʡʡʡʡʡʡʡʡʡʡʡʡ�\\n�z�w�w�w�w�w�w�w�w�w�w�w�w�w�w�{\\n�x�i���ܡj�Ҧ������ҳ���������x\\n�|�w�w�w�w�w�w�w�w�w�w�w�w�w�w�}\\n�Ҧp�G\\n�@�� ~\!b\!~ �N���������@�� ~\!/b\!~\')\;\n";
 print "  my.msg.focus()\;\n";
 print "  return false\;\n";
 print " }\n";
 print "}\n";
 print "function codecount(codestr)\n";
 print "{\n";
 print " var count=0\;\n";
 print " var index=0\;\n";
 print " while(my.msg.value.indexOf(codestr,index)!=-1)\n";
 print " {\n";
 print "  count++\;\n";
 print "  index=my.msg.value.indexOf(codestr,index)+1\;\n";
 print " }\n";
 print " return count\n";
 print "}\n";
 print "</SCRIPT>\n";
 print "</HEAD>\n";
 print "<BODY BGCOLOR=$bgcolor ONLOAD=my.msg.focus()>\n";
 print "<FORM NAME=my ACTION=$cgiurl METHOD=post ONSUBMIT=return(codecheck())\;>\n";
 print "<TABLE CELLSPACING=3 ALIGN=CENTER STYLE=text-align:center\;font-size:8pt>\n";
 print "<TR><TD STYLE=position:relative\;color:white\;font-size:8pt\;text-decoration:underline\;letter-spacing:5px\;filter:glow(color=red,strength=1)\;>�ǰe�T��</TD><TR>\n";
 print "<TR><TD>���G<FONT COLOR=coral>$reciever[1]�i$reciever[0]�j</FONT></TD></TR>\n";
 print "<TR><TD><INPUT TYPE=text NAME=msg SIZE=10 STYLE=font-size:8pt\;color:green\;border-width:3px\;border-style:double\;border-color:darkcyan></TD></TR>\n";
 print "<TR><TD><INPUT TYPE=submit VALUE=�T�w STYLE=font-size:8pt\;color:brown\;background-color:powderblue\;border-width:1px\;border-style:solid\;border-color:darkcyan\;>\n";
 print "<INPUT TYPE=reset VALUE=�M�� STYLE=font-size:8pt\;color:brown\;background-color:powderblue\;border-width:1px\;border-style:solid\;border-color:darkcyan></TD></TR>\n";
 print "</TABLE>\n";
 print "<INPUT TYPE=hidden NAME=job VALUE=savemsg>\n";
 print "<INPUT TYPE=hidden NAME=sender VALUE=\'$FORM{sender}�i$ip�j\'>\n";
 print "<INPUT TYPE=hidden NAME=reciever VALUE=\'$reciever[0]\'>\n";
 print "</FORM>\n";
 print "<HR><CENTER><input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;></CENTER>";
 print "</BODY></HTML>\n";
}
#########################################################################
sub savemsg
{
 ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time);
 $mon++;
 ##-----�L�o���X�k�r��
 if(substr($FORM{msg},0,7) ne $usehtmlpass)
 {
  $FORM{msg}=~s/</&lt\;/g;
  $FORM{msg}=~s/>/&gt\;/g;
 }
 else
 {
  $FORM{msg}=substr($FORM{msg},7);
 }
 $FORM{msg}=~s/��/||/g;
 $FORM{msg}=~s/\'/\\\'/g;
 $FORM{msg}=~s/\"/\\\"/g;
 ##�ഫ�S��html�y�k
 $FORM{msg}=~s/~!red!~/<font color=red>/g;
 $FORM{msg}=~s/~!blue!~/<font color=blue>/g;
 $FORM{msg}=~s/~!green!~/<font color=green>/g;
 $FORM{msg}=~s/~!purple!~/<font color=purple>/g;
 $FORM{msg}=~s/~!dodgerblue!~/<font color=dodgerblue>/g;
 $FORM{msg}=~s/~!deeppink!~/<font color=deeppink>/g;
 $FORM{msg}=~s/~!lightgreen!~/<font color=lightgreen>/g;
 $FORM{msg}=~s/~!mediumpurple!~/<font color=mediumpurple>/g;
 $FORM{msg}=~s/~!sienna!~/<font color=sienna>/g;
 $FORM{msg}=~s/~!olivedrab!~/<font color=olivedrab>/g;
 $FORM{msg}=~s/~!big!~/<big>/g;
 $FORM{msg}=~s/~!small!~/<small>/g;
 $FORM{msg}=~s/~!i!~/<i>/g;
 $FORM{msg}=~s/~!b!~/<b>/g;
 $FORM{msg}=~s/~!\/color!~/<\/font>/g;
 $FORM{msg}=~s/~!\/big!~/<\/big>/g;
 $FORM{msg}=~s/~!\/small!~/<\/small>/g;
 $FORM{msg}=~s/~!\/i!~/<\/i>/g;
 $FORM{msg}=~s/~!\/b!~/<\/b>/g;
 ##-----
 open (FILE, $datafile);@DATAS=<FILE>;close (FILE);
 open(FILE,">$datafile");
 foreach $line (@DATAS)
 {
  ($recip,$recadd,$recmsgonoff,$rectime,$recintime,$recnick,$recmsg)=split("��",$line);
  chop $recmsg;
  $newmsg="";
  if(($FORM{reciever} eq "all") and ($ip ne $recip) and ($recmsgonoff eq "on"))
  {
   $found=1;
   if($recmsg ne "")
   {
    $newmsg=$recmsg."<HR>";
   }
   $newmsg=$newmsg."<FONT COLOR=blueviolet>".$FORM{sender}."</FONT> ��<SPAN STYLE=text-decoration:underline>�T���s��</SPAN>�G<BR>".$FORM{msg}."<BR><DIV STYLE=text-align:right\;color:gray\;font-size:8pt>\&lt\; ".$mon."/".$mday." ".$hour.":".$min.":".$sec." \&gt\;</DIV>";
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$recnick��$newmsg\n";
  }
  elsif(($FORM{reciever} eq $recip) and ($recmsgonoff eq "on"))
  {
   $found=1;
   if($recmsg ne "")
   {
    $newmsg=$recmsg."<HR>";
   }
   $newmsg=$newmsg."����Ӧ� <FONT COLOR=9966ff>".$FORM{sender}."</FONT> ��<SPAN STYLE=text-decoration:underline>�T��</SPAN>�G<BR>".$FORM{msg}."<BR><DIV STYLE=text-align:right\;color:gray\;font-size:8pt>\&lt\; ".$mon."/".$mday." ".$hour.":".$min.":".$sec." \&gt\;</DIV>";
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$recnick��$newmsg\n";
  }
  else
  {
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$recnick��$recmsg\n";
  }
 }
 close(FILE);
 print "Content-type: text/html\n\n";
 if($found eq 1){print "<SCRIPT LANGUAGE=JavaScript>\nwindow.close()\;\n</SCRIPT>\n";}
 else
 {
  print "<HTML><HEAD><meta http-equiv=\"Content-Type\" content=\"text/html\; charset=big5\"><TITLE>�ǰe�T���o�Ϳ��~</TITLE></HEAD>\n";
  print "<BODY BGCOLOR=$bgcolor><CENTER>\n";
  print "<TABLE><TR><TD STYLE=position:relative\;color:white\;font-size:8pt\;text-decoration:underline\;letter-spacing:5px\;filter:glow(color=red,strength=1)\;>���~�T��</TD></TR></TABLE><BR>\n";
  print "<DIV STYLE=font-size:8pt\;color:darkred\;text-align:left>�ǰe�T���ɵo�Ϳ��~�I<BR>���~�o�ͭ�]�i�ର�G<BR>�����T�̪����T�}�����y���z<BR>�����T�̤w�g���b���W<BR>���Y���T���s���h��ܨ�L�H<BR>�����T�}���Ҭ��y���z</DIV>\n";
  print "<HR><CENTER><input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;>";
  print "</CENTER></BODY></HTML>\n";
 }
}
#########################################################################
sub chgmsgonoff
{
 open (FILE, $datafile);@DATAS=<FILE>;close (FILE);
 open(FILE,">$datafile");
 foreach $line (@DATAS)
 {
  ($recip,$recadd,$recmsgonoff,$rectime,$recintime,$recnick,$recmsg)=split("��",$line);
  chop $recmsg;
  if($ip eq $recip)
  {
   if($recmsgonoff eq "on"){print FILE "$recip��$recadd��off��$rectime��$recintime��$recnick��$recmsg\n";}
   else{print FILE "$recip��$recadd��on��$rectime��$recintime��$recnick��$recmsg\n";}
  }
  else
  {
   print FILE "$recip��$recadd��$recmsgonoff��$rectime��$recintime��$recnick��$recmsg\n";
  }
 }
 close(FILE);
 &main;
}
#########################################################################
sub show
{
 open (FILE, $datafile);@DATAS=<FILE>;close (FILE);
 print "Content-type: text/html\n\n";
 print "<HTML><HEAD><meta http-equiv=\"Content-Type\" content=\"text/html\; charset=big5\"><TITLE>�ԲӸ��</TITLE></HEAD>\n";
 print "<BODY BGCOLOR=$bgcolor><CENTER>\n";
 print "<TABLE><TR><TD STYLE=position:relative\;color:white\;font-size:8pt\;text-decoration:underline\;letter-spacing:5px\;filter:glow(color=red,strength=1)\;>�ԲӸ��</TD></TR></TABLE><BR>\n";
 print "<input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;><HR>";
 print "<TABLE BORDER=1 STYLE=font-size:8pt\;text-align:center><TR><TD>�ʺ�<BR>�iIP/�D���W�١j</TD><TD>�W���ɶ�</TD><TD>���o�T��<BR>���A</TD><TD>���L�T��</TD></TR>\n";
 foreach $line (@DATAS)
 {
  ($recip,$recadd,$recmsgonoff,$rectime,$recintime,$recnick,$recmsg)=split("��",$line);
  chop $recmsg;
  print "<TR><TD><FONT COLOR=darkcyan>$recnick</FONT><BR><FONT COLOR=darkseagreen>�i$recip/$recadd�j</FONT></TD><TD>$recintime</TD>";
  if($recmsgonoff eq "on")
  {
   print "<TD><FONT COLOR=red>�}</FONT></TD>";
  }
  else
  {
   print "<TD>��</TD>";
  }
  if($recmsg eq "")
  {
   print "<TD>�L</TD></TR>\n";
  }
  else
  {
   print "<TD><FONT COLOR=red>��</FONT></TD></TR>\n";
  }
 }
 print "\n";
 print "</TABLE>\n";
 print "<HR><input type=button value=\"��������\" STYLE=font-size:8pt\;color:blue\; onclick=window.close()\;></CENTER>";
 print "</CENTER></BODY></HTML>\n";
}
#########################################################################
sub readme
{
 print "Content-type: text/html\n\n";
print <<HTML;
 <HTML><HEAD><meta http-equiv="Content-Type" content="text/html; charset=big5"><TITLE>TMmany �u�W�ǰT v 1.2.3</TITLE>
<STYLE TYPE="text/css">
.maintab {background-color:peachpuff;border-color:lightcoral;border-width:4px;border-style:double;font-size:8pt;text-align:center}
.maintab td {background-color:lightgoldenrodyellow;border-color:lightpink;border-width:1px;border-style:solid;line-height:18px}
.maintab table td {font-size:8pt;text-align:center;border-width:0px;line-height:15px}
</STYLE>
</HEAD>
<BODY BGCOLOR=F0FFF0><CENTER>
<TABLE><TR><TD STYLE=position:relative;color:white;font-size:8pt;text-decoration:underline;letter-spacing:5px;filter:glow(color=red,strength=1);>�����ɮ�</TD></TR></TABLE><BR>
<input type=button value="��������" STYLE=font-size:8pt;color:blue; onclick=window.close();><HR>
<TABLE CLASS=maintab CELLSPACING=1 CELLPADDING=2>
<TR HEIGHT=50><TH COLSPAN=2 STYLE=position:relative;color:bisque;font-size:8pt;text-decoration:underline;letter-spacing:5px;filter:glow(color=blue,strength=1);>TMmany �u�W�ǰT v 1.2.3</TD></TR>
<TR><TD STYLE=background-color:paleturquoise;color:teal>�{���@��</TD><TD STYLE=background-color:paleturquoise;color:teal><a href=mailto:turtlemn\@pchome.com.tw>TurtleMan</a></TD></TR>
<TR><TD COLSPAN=2><FONT COLOR=GREEN>���@�{�������@��</FONT></TD></TR>
<TR><TD COLSPAN=2 ALIGN=LEFT>
<FONT COLOR=navy>���u�W�H�ƭp��</FONT><BR>
�@<FONT COLOR=royalblue>���F�ǲΪ���ܥثe�u�W���H�Ƥ��~�A�٥i�H�d�߽u�W�ӤH���ԲӸ�ơA<BR>
�@�]�t�ʺ١BIP�B�D���W�١B�W���ɶ��B���T���A�H�ΰT���}���C</FONT><BR>
�@<FONT COLOR=orchid>���ʺ١G</FONT><BR>
�@<FONT COLOR=orangered>��</FONT>�ϥ� Cookie �C�����ʺٮɱN�ȼg�J�A�C���W���Y�۰ʥ� Cookie ��Ū<BR>
�@�@���W���]�w���ʺ١A�i�H���ΨC���W�����s��g�C<BR>
�@<FONT COLOR=orangered>��</FONT>�ʺ٪��]�w���׳̪������Ӥ���r�q���Φr�r�΢����ӭ^�Ʀr�q�b�Φr�r<BR>
�@�@�A�i�H�����ϥΡC<BR>
<FONT COLOR=navy>���u�W�ǰe�T��</FONT><BR>
�@<FONT COLOR=royalblue>�i�H��ܹ��H�o�e�T���ΥH�T���s�����Φ���h�H�P�ɵo�e�T��</FONT><BR>
�@<FONT COLOR=orchid>����H�ǰT�G</FONT><BR>
�@<FONT COLOR=orangered>��</FONT>�����b�U�Կ�椤�I��n�o�e����H�N�|�X�{��g�T���������A��g��<BR>
�@�@����e�X�Y�����o�T�ʧ@�C<BR>
�@<FONT COLOR=orangered>��</FONT>���F�קK���H�y�G�N�z�b�T�����[�J�}�a�y�k�A�]���T�����Ҧ���HTML<BR>
�@�@���ҳ��|�L�k��ܡF���O�A�٬O�i�H��ΤU����HTML���N�y�k�Өϥ�²<BR>
�@�@�檺�y�k�C<BR>
�@<FONT COLOR=orchid>���T���s���G</FONT><BR>
�@<FONT COLOR=orangered>��</FONT>�b�U�Կ�椤�I��T���s���ﶵ�N�|�X�{��g�T���������A��g������<BR>
�@�@�e�X�Y�����s���ʧ@�C<BR>
�@<FONT COLOR=orangered>��</FONT>�T���s�������T��H���G���F�A�H�~�Ҧ����T�}�����y�}�z���u�W�H��<BR>
�@<FONT COLOR=orangered>��</FONT>���F�קK���H�y�G�N�z�b�T�����[�J�}�a�y�k�A�]���T�����Ҧ���HTML<BR>
�@�@���ҳ��|�L�k��ܡF���O�A�٬O�i�H��ΤU����HTML���N�y�k�Өϥ�²<BR>
�@�@�檺�y�k�C<BR>
</TD></TR>
<TR><TD COLSPAN=2><FONT COLOR=GREEN>���@���N�y�k�@��</FONT></TD></TR>
<TR><TD COLSPAN=2>
<FONT COLOR=RED>��</FONT><FONT COLOR=crimson>�Ҧ����Ҫ��@�νd��N�b�_�l���Ҥε������Ҥ�<BR>
�@�]���Ҧ������ҳ���������X�{�I</FONT>
  <TABLE WIDTH=90%>
  <TR><TD>�_�l����</TD><TD>��������</TD><TD>����</TD></TR>
  <TR><TD>~!red!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=red>��</FONT>��</TD></TR>
  <TR><TD>~!blue!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=blue>��</FONT>��</TD></TR>
  <TR><TD>~!green!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=green>��</FONT>��</TD></TR>
  <TR><TD>~!purple!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=purple>��</FONT>��</TD></TR>
  <TR><TD>~!dodgerblue!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=dodgerblue>��</FONT>��</TD></TR>
  <TR><TD>~!deeppink!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=deeppink>��</FONT>��</TD></TR>
  <TR><TD>~!lightgreen!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=lightgreen>��</FONT>��</TD></TR>
  <TR><TD>~!mediumpurple!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=mediumpurple>��</FONT>��</TD></TR>
  <TR><TD>~!olivedrab!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=olivedrab>��</FONT>��</TD></TR>
  <TR><TD>~!sienna!~</TD><TD>~!/color!~</TD><TD>�]�w�r�鬰<FONT COLOR=sienna>��</FONT>��</TD></TR>
  <TR><TD>~!big!~</TD><TD>~!/big!~</TD><TD>��j�r��</TD></TR>
  <TR><TD>~!small!~</TD><TD>~!/small!~</TD><TD>�Y�p�r��</TD></TR>
  <TR><TD>~!i!~</TD><TD>~!/i!~</TD><TD>����r</TD></TR>
  <TR><TD>~!b!~</TD><TD>~!/b!~</TD><TD>����r</TD></TR>
  </TABLE><BR>
�i�d��-��J�j
<DIV STYLE=font-size:8pt;color:black;text-align:left;width:80%>�o~!red!~~!big!~�O~!/big!~~!i!~�@��~!/i!~<BR>~!/color!~²~!green!~��~!deeppink!~��~!/color!~�d~!/color!~�ҡI</DIV>
�i��ܪ��ĪG�j
<DIV STYLE=font-size:8pt;color:black;text-align:left;width:80%>�o<FONT COLOR=red><BIG>�O</BIG><I>�@��</I></FONT>²<FONT COLOR=green>��<FONT COLOR=deeppink>��</FONT>�d</FONT>�ҡI</DIV>
</TD></TR>
</TABLE>
<HR><input type=button value="��������" STYLE=font-size:8pt;color:blue; onclick=window.close();>
</CENTER></BODY></HTML>
HTML
}
#########################################################################
sub get_form
{
 my (@pairs,@querys,%in);
 my ($buffer, $pair, $name, $value);
 @querys = split(/&/, $ENV{'QUERY_STRING'});
 foreach (@querys)
 {
  ($name,$value) = split(/=/, $_);
  $name  = &decode($name);
  $value = &decode($value);
  %in=&setvaluetoform($name, $value); 
 }
 read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 @pairs = split(/&/, $buffer);
 foreach (@pairs)
 {
  ($name, $value) = split(/=/, $_);
  push (@make, $value) if ($name eq "mark");
  $name  = &decode($name);
  $value = &decode($value);
  %in=&setvaluetoform($name, $value); 
 }
 return %in;
}
#########################################################################
sub decode
{
 local($return)=$_[0];
 $return =~ tr/+/ /;
 $return =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
 return $return;
}
#########################################################################
sub setvaluetoform
{
 if ($FORM{$_[0]})
 {
  $FORM{$_[0]}="$FORM{$_[0]}��$_[1]";
 }
 else
 {
  $FORM{$_[0]}=$_[1];
 }
 return %FORM;
}
#########################################################################
sub set_cookie {
($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg)= gmtime(time + 60*24*60*60);

$yearg += 1900;
if ($secg < 10) { $secg = "0$secg"; }
if ($ming < 10) { $ming = "0$ming"; }
if ($hourg < 10) { $hourg = "0$hourg"; }
if ($mdayg < 10) { $mdayg = "0$mdayg"; }

$month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
$youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
$date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
$cook="nick��$FORM{nick}\,email��emailemail";
print "Set-Cookie: TMmany=$cook; expires=$date_gmt\n";
}
#########################################################################
sub get_cookie { 
@pairs = split(/\;/, $ENV{'HTTP_COOKIE'});
foreach $pair (@pairs) {
local($name, $value) = split(/\=/, $pair);
$name =~ s/ //g;
$DUMMY{$name} = $value;
}
@pairs = split(/\,/, $DUMMY{'TMmany'});
foreach $pair (@pairs) {
local($name, $value) = split(/\��/, $pair);
$COOKIE{$name} = $value;
}
	$cookienick  = $COOKIE{'nick'};
}