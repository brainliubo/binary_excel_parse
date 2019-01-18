# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"binary_excel_parse", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		total_boxsizer = wx.BoxSizer( wx.VERTICAL )

		excel_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.excel_statictext = wx.StaticText( excel_sizer.GetStaticBox(), wx.ID_ANY, u"excel file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.excel_statictext.Wrap( -1 )

		excel_sizer.Add( self.excel_statictext, 0, wx.ALL, 5 )

		self.excel_filePicker = wx.FilePickerCtrl( excel_sizer.GetStaticBox(), wx.ID_ANY, u"C:\\Users\\brain.liu\\Desktop\\DP_FEC 模块测试问题日志.xlsx", u"Select a file", u"*.xls;*.xlsx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		excel_sizer.Add( self.excel_filePicker, 10, wx.ALL, 5 )

		self.excel_check_button = wx.Button( excel_sizer.GetStaticBox(), wx.ID_ANY, u"check", wx.DefaultPosition, wx.DefaultSize, 0 )
		excel_sizer.Add( self.excel_check_button, 3, wx.ALL, 5 )


		total_boxsizer.Add( excel_sizer, 1, wx.EXPAND, 5 )

		binary_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.excel_statictext1 = wx.StaticText( binary_sizer.GetStaticBox(), wx.ID_ANY, u"binary file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.excel_statictext1.Wrap( -1 )

		binary_sizer.Add( self.excel_statictext1, 0, wx.ALL, 5 )

		self.binay_filePicker = wx.FilePickerCtrl( binary_sizer.GetStaticBox(), wx.ID_ANY, u"C:\\Users\\brain.liu\\Desktop\\256QAM 星座点.xlsx", u"Select a file", u"*.dat;*.bin", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		binary_sizer.Add( self.binay_filePicker, 10, wx.ALL, 5 )

		self.binary_check_button = wx.Button( binary_sizer.GetStaticBox(), wx.ID_ANY, u"check", wx.DefaultPosition, wx.DefaultSize, 0 )
		binary_sizer.Add( self.binary_check_button, 3, wx.ALL, 5 )


		total_boxsizer.Add( binary_sizer, 1, wx.EXPAND, 5 )


		bSizer1.Add( total_boxsizer, 1, wx.EXPAND, 5 )

		parse_boxsizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.parse_config = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"Parse_config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parse_config.Wrap( -1 )

		parse_boxsizer.Add( self.parse_config, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText22 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"二进制文件大小", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer2.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.binary_file_size_textctrl = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.binary_file_size_textctrl, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"unit:byte", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer2.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"二进制文件端模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer2.Add( self.m_staticText51, 0, wx.ALL, 5 )

		parse_choiceChoices = [ u"小端模式", u"大端模式" ]
		self.parse_choice = wx.Choice( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, parse_choiceChoices, 0 )
		self.parse_choice.SetSelection( 1 )
		fgSizer2.Add( self.parse_choice, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 3, wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"解析单元长度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer2.Add( self.m_staticText68, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl7, 5, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"uint:byte", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer2.Add( self.m_staticText34, 2, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"解析单元个数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl8, 5, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer2.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"循环解析次数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.loop_textctrl = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loop_textctrl.SetMaxLength( 100 )
		fgSizer2.Add( self.loop_textctrl, 5, wx.ALL, 5 )

		self.loop_checkBox = wx.CheckBox( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"循环解析", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loop_checkBox.SetValue(True)
		fgSizer2.Add( self.loop_checkBox, 0, wx.ALL, 5 )


		parse_boxsizer.Add( fgSizer2, 1, wx.EXPAND, 5 )


		bSizer1.Add( parse_boxsizer, 1, wx.EXPAND, 5 )

		sbSizer62 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m_staticText = wx.StaticText( sbSizer62.GetStaticBox(), wx.ID_ANY, u"output_config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText.Wrap( -1 )

		sbSizer62.Add( self.m_staticText, 0, wx.ALL, 5 )

		total_boxsizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer63 = wx.StaticBoxSizer( wx.StaticBox( sbSizer62.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m_staticText93 = wx.StaticText( sbSizer63.GetStaticBox(), wx.ID_ANY, u"输出文件格式选择", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		sbSizer63.Add( self.m_staticText93, 0, wx.ALL, 5 )

		output_choiceChoices = [ u"excel文件", u"文本文件" ]
		self.output_choice = wx.Choice( sbSizer63.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, output_choiceChoices, 0 )
		self.output_choice.SetSelection( 0 )
		sbSizer63.Add( self.output_choice, 0, wx.ALL, 5 )


		total_boxsizer1.Add( sbSizer63, 1, wx.EXPAND, 5 )

		output_excel_sizer = wx.StaticBoxSizer( wx.StaticBox( sbSizer62.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.output_statictext = wx.StaticText( output_excel_sizer.GetStaticBox(), wx.ID_ANY, u"excel file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_statictext.Wrap( -1 )

		output_excel_sizer.Add( self.output_statictext, 2, wx.ALL, 5 )

		self.output_excel_textctrl = wx.TextCtrl( output_excel_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		output_excel_sizer.Add( self.output_excel_textctrl, 10, wx.ALL, 5 )

		self.output_excel_filePicker = wx.FilePickerCtrl( output_excel_sizer.GetStaticBox(), wx.ID_ANY, u"C:\\Users\\brain.liu\\Desktop\\附件2-6.xlsx", u"Select a file", u"*.xlsx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL )
		output_excel_sizer.Add( self.output_excel_filePicker, 1, wx.ALL, 5 )


		total_boxsizer1.Add( output_excel_sizer, 1, wx.EXPAND, 5 )

		output_log_sizer = wx.StaticBoxSizer( wx.StaticBox( sbSizer62.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.output_log_statictext = wx.StaticText( output_log_sizer.GetStaticBox(), wx.ID_ANY, u"log file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_log_statictext.Wrap( -1 )

		output_log_sizer.Add( self.output_log_statictext, 2, wx.ALL, 5 )

		self.output_log_textctrl = wx.TextCtrl( output_log_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		output_log_sizer.Add( self.output_log_textctrl, 10, wx.ALL, 5 )

		self.output_excel_filePicker1 = wx.FilePickerCtrl( output_log_sizer.GetStaticBox(), wx.ID_ANY, u"C:\\Users\\brain.liu\\Desktop\\附件2-6.xlsx", u"Select a file", u"*.log", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL )
		output_log_sizer.Add( self.output_excel_filePicker1, 1, wx.ALL, 5 )


		total_boxsizer1.Add( output_log_sizer, 1, wx.EXPAND, 5 )


		sbSizer62.Add( total_boxsizer1, 10, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer62, 1, wx.EXPAND, 5 )

		apply = wx.StdDialogButtonSizer()
		self.applyApply = wx.Button( self, wx.ID_APPLY )
		apply.AddButton( self.applyApply )
		apply.Realize();

		bSizer1.Add( apply, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.excel_check_button.Bind( wx.EVT_BUTTON, self.excel_check )
		self.binay_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.binary_file_read )
		self.parse_choice.Bind( wx.EVT_CHOICE, self.parse_choise_selected )
		self.loop_checkBox.Bind( wx.EVT_CHECKBOX, self.loop_parse_check )
		self.output_choice.Bind( wx.EVT_CHOICE, self.output_choice_select )
		self.output_excel_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.output_excel_changed )
		self.output_excel_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.output_excel_changed )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def excel_check( self, event ):
		event.Skip()

	def binary_file_read( self, event ):
		event.Skip()

	def parse_choise_selected( self, event ):
		event.Skip()

	def loop_parse_check( self, event ):
		event.Skip()

	def output_choice_select( self, event ):
		event.Skip()

	def output_excel_changed( self, event ):
		event.Skip()



