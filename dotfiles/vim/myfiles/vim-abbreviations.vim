iabbrev libp use lib qw/perl_modules_02 perl_modules_01/;<ESC>

" Print abbreviations
iabbrev pp print "\n\n", ,"\n\n";<ESC><S-B><Insert>
iabbrev dd print "\n\n",Data::Dumper->Dump([ ]),"\n\n";<ESC><S-B><Insert>
iabbrev ddf print "<pre>",Data::Dumper->Dump([ ]),"</pre>";<ESC><S-B><Insert>
iabbrev ddb print STDERR "\n\n",Data::Dumper->Dump([ ]),"\n\n";<ESC><S-B><Insert>

" Blocks abbreviations
iabbrev attrp <%attr><CR></%attr><ESC>ko
iabbrev argsp <%args><CR></%args><ESC>ko
iabbrev flagsp <%flags><CR>inherit=>'/syshandler'<CR></%flags><CR>
iabbrev filterp <%filter><CR>unless($m->aborted()){<CR>$_ = Utils::FillInForm->new->fill ( scalarref => \$_, fdat =>   \%ARGS,);<CR>}<CR></%filter><CR>
iabbrev perlp <%perl><CR></%perl><ESC>ko
iabbrev docp <%doc><CR></%doc><ESC>ko

" Jquery abbreviations 
iabbrev changep $(document).on("","change",function(){<cr>});<ESC>kf(l
iabbrev clickp $(document).on("","click",function(){<cr>});<ESC>kf(l
iabbrev submitp $(document).on("","submit",function(){<cr>});<ESC>kf(l
iabbrev readyp $(document).ready(function(){<cr>});<ESC>ko
iabbrev scriptp <script><CR></script><ESC>ko
iabbrev scriptpp <script type='text/javascript' src="<% &Conf::SEC_STATIC_SERVER %>"></script><ESC>FE 
iabbrev linkp <link href="<% &Conf::SEC_STATIC_SERVER %>" rel="stylesheet" type="text/css"><ESC>FR


" Database abbreviations 
iabbrev dbhp my $dbh = &Utils::db_connect();
iabbrev dbhpp my $dbh = &UtilsDB::db_connect('ATTR'=>{ 'AutoCommit'=>1, 'RaiseError'=>1, pg_server_prepare=>0 });
iabbrev beginp &UtilsDB::db_begin(dbh=>$dbh,txn_params=>$b2bglobal{txn_params});
iabbrev commitp &UtilsDB::db_commit(dbh => $dbh);
iabbrev rollbackp &UtilsDB::db_rollback(dbh => $dbh);

iabbrev schemap my $dbix_schema = DBSchema:__SCHEMA__->connect(sub { &UtilsDB::db_connect(ATTR=>{'AutoCommit'=>1, 'RaiseError'=>1, pg_server_prepare=>0}) },{on_connect_do => ['SET search_path =public,general; SET default_transaction_read_only TO false;']});
iabbrev rsp my $rs = $dbix_schema->resultset('');<ESC>hhi


" b2bglobal vars abbreviations
iabbrev b2bp  $b2bglobal{}<Left>
iabbrev b2bcup  $b2bglobal{current_user}
iabbrev b2bcep  $b2bglobal{current_employee}
iabbrev b2bcpp  $b2bglobal{current_profile}

" Objects Related abbreviations
iabbrev companyp my $company = new B2B::Company(dbh=>$dbh_ro,profile_id=>$profile_id);
iabbrev userp my $user = new B2B::User(dbh=>$dbh_ro,userid=>$userid);
iabbrev employeep  my $employee = new Erp::Employee($dbh_ro,$user_id);
iabbrev mobilep my $mobile = new B2B::Mobile(dbh=>$dbh , mobile=> );<ESC>F>
iabbrev emailp my $email = new B2B::Email (dbh=>$dbh , email=> );<ESC>F>
iabbrev datep my $date = new B2B::Date($dbh_ro,$date_id);
iabbrev categoryp my $category = new B2B::Category($dbh_ro,$category_id);

" Coding Related abbreviations
iabbrev ifp  if(){<CR>}<Esc>kf(a
iabbrev unlessp  if(){<CR>}<Esc>kf(a
iabbrev whilep  while(){<CR>}<Esc>kf(a
iabbrev forp foreach(){<CR>}<Esc>kf(a

" Others abbreviations
iabbrev =>p => undef
iabbrev ii  <%%><ESC>0f%a
"nnoremap <leader>ii <% %><ESC>hhi 


""" 
" iabbrev sthp my $sth = $dbh -> prepare("");<Esc>F"i
" iabbrev sthee $sth->execute();<Esc>F(i
""" 




