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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"binary_excel_parse_tool", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		excel_boxsizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		excel_sizer1 = wx.StaticBoxSizer( wx.StaticBox( excel_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m_staticText46 = wx.StaticText( excel_sizer1.GetStaticBox(), wx.ID_ANY, u"excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		excel_sizer1.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.excel_filePicker = wx.FilePickerCtrl( excel_sizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.xls;*.xlsx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		excel_sizer1.Add( self.excel_filePicker, 10, wx.ALL, 5 )

		self.excel_check_button = wx.Button( excel_sizer1.GetStaticBox(), wx.ID_ANY, u"格式检查", wx.DefaultPosition, wx.DefaultSize, 0 )
		excel_sizer1.Add( self.excel_check_button, 0, wx.ALL, 5 )


		excel_boxsizer.Add( excel_sizer1, 1, wx.EXPAND, 5 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.sheet_staticText1 = wx.StaticText( excel_boxsizer.GetStaticBox(), wx.ID_ANY, u" sheet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sheet_staticText1.Wrap( -1 )

		bSizer41.Add( self.sheet_staticText1, 0, wx.ALL, 5 )

		sheet_choiceChoices = [ wx.EmptyString, wx.EmptyString, u" ", u" ", u" ", wx.EmptyString, wx.EmptyString, wx.EmptyString ]
		self.sheet_choice = wx.Choice( excel_boxsizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sheet_choiceChoices, 0 )
		self.sheet_choice.SetSelection( 0 )
		bSizer41.Add( self.sheet_choice, 1, wx.ALL, 5 )

		self.row_start_staticText1 = wx.StaticText( excel_boxsizer.GetStaticBox(), wx.ID_ANY, u"start_row", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.row_start_staticText1.Wrap( -1 )

		bSizer41.Add( self.row_start_staticText1, 0, wx.ALL, 5 )

		self.startrow_textCtrl = wx.TextCtrl( excel_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer41.Add( self.startrow_textCtrl, 1, wx.ALL, 5 )

		self.m_staticText371 = wx.StaticText( excel_boxsizer.GetStaticBox(), wx.ID_ANY, u"end_row", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		bSizer41.Add( self.m_staticText371, 0, wx.ALL, 5 )

		self.endrow_textCtrl = wx.TextCtrl( excel_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer41.Add( self.endrow_textCtrl, 1, wx.ALL, 5 )


		bSizer51.Add( bSizer41, 1, wx.EXPAND, 5 )


		excel_boxsizer.Add( bSizer51, 1, wx.EXPAND, 5 )


		bSizer1.Add( excel_boxsizer, 1, wx.ALL|wx.EXPAND, 5 )

		parse_boxsizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		binary_sizer = wx.StaticBoxSizer( wx.StaticBox( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.excel_statictext1 = wx.StaticText( binary_sizer.GetStaticBox(), wx.ID_ANY, u"binary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.excel_statictext1.Wrap( -1 )

		binary_sizer.Add( self.excel_statictext1, 0, wx.ALL, 5 )

		self.binary_filePicker = wx.FilePickerCtrl( binary_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.dat;*.bin", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		binary_sizer.Add( self.binary_filePicker, 10, wx.ALL, 5 )

		self.parse_check_button = wx.Button( binary_sizer.GetStaticBox(), wx.ID_ANY, u"文件读取", wx.DefaultPosition, wx.DefaultSize, 0 )
		binary_sizer.Add( self.parse_check_button, 0, wx.ALL, 5 )


		parse_boxsizer.Add( binary_sizer, 0, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 6, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText22 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"二进制文件大小", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer2.Add( self.m_staticText22, 0, wx.ALL|wx.EXPAND, 5 )

		self.binary_file_size_textctrl = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer2.Add( self.binary_file_size_textctrl, 1, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"unit:byte", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer2.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"二进制文件端模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer2.Add( self.m_staticText51, 0, wx.ALL, 5 )

		ending_choiceChoices = [ u" ", u"小端模式", u"大端模式", wx.EmptyString, wx.EmptyString ]
		self.ending_choice = wx.Choice( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,-1 ), ending_choiceChoices, 0 )
		self.ending_choice.SetSelection( 1 )
		fgSizer2.Add( self.ending_choice, 5, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 3, wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"解析单元长度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer2.Add( self.m_staticText68, 0, wx.ALL, 5 )

		parse_unit_choiceChoices = [ u" ", u"32", u"64", u"96", u"128", u"192", u"256", wx.EmptyString, wx.EmptyString ]
		self.parse_unit_choice = wx.Choice( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, parse_unit_choiceChoices, 0 )
		self.parse_unit_choice.SetSelection( 0 )
		fgSizer2.Add( self.parse_unit_choice, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"uint:bit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer2.Add( self.m_staticText34, 2, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"解析单元个数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )

		self.parse_number_textCtrl = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer2.Add( self.parse_number_textCtrl, 5, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer2.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"循环解析次数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.loop_textctrl = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.loop_textctrl.SetMaxLength( 100 )
		fgSizer2.Add( self.loop_textctrl, 5, wx.ALL, 5 )

		self.loop_checkBox = wx.CheckBox( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"循环解析", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.loop_checkBox, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( parse_boxsizer.GetStaticBox(), wx.ID_ANY, u"循环最大次数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.max_loop_textCtrl = wx.TextCtrl( parse_boxsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.max_loop_textCtrl, 0, wx.ALL, 5 )


		parse_boxsizer.Add( fgSizer2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( parse_boxsizer, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer62 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		total_boxsizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer63 = wx.StaticBoxSizer( wx.StaticBox( sbSizer62.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m_staticText20 = wx.StaticText( sbSizer63.GetStaticBox(), wx.ID_ANY, u"输出数据格式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		sbSizer63.Add( self.m_staticText20, 0, wx.ALL, 5 )

		output_data_format_choiceChoices = [ u"十六进制", u"十进制", wx.EmptyString ]
		self.output_data_format_choice = wx.Choice( sbSizer63.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, output_data_format_choiceChoices, 0 )
		self.output_data_format_choice.SetSelection( 0 )
		sbSizer63.Add( self.output_data_format_choice, 1, wx.ALL, 5 )

		self.m_staticText93 = wx.StaticText( sbSizer63.GetStaticBox(), wx.ID_ANY, u"输出文件格式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		sbSizer63.Add( self.m_staticText93, 0, wx.ALL, 5 )

		output_choiceChoices = [ u"excel文件" ]
		self.output_choice = wx.Choice( sbSizer63.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, output_choiceChoices, 0 )
		self.output_choice.SetSelection( 0 )
		sbSizer63.Add( self.output_choice, 1, wx.ALL, 5 )


		total_boxsizer1.Add( sbSizer63, 1, wx.EXPAND, 5 )

		output_excel_sizer = wx.StaticBoxSizer( wx.StaticBox( sbSizer62.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.output_statictext = wx.StaticText( output_excel_sizer.GetStaticBox(), wx.ID_ANY, u"excel file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_statictext.Wrap( -1 )

		output_excel_sizer.Add( self.output_statictext, 2, wx.ALL, 5 )

		self.output_excel_filePicker = wx.FilePickerCtrl( output_excel_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.xlsx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		output_excel_sizer.Add( self.output_excel_filePicker, 12, wx.ALL, 5 )


		total_boxsizer1.Add( output_excel_sizer, 1, wx.EXPAND, 5 )

		output_log_sizer = wx.StaticBoxSizer( wx.StaticBox( sbSizer62.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.output_log_statictext = wx.StaticText( output_log_sizer.GetStaticBox(), wx.ID_ANY, u"log file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_log_statictext.Wrap( -1 )

		output_log_sizer.Add( self.output_log_statictext, 2, wx.ALL, 5 )

		self.output_log_filePicker = wx.FilePickerCtrl( output_log_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.log", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		output_log_sizer.Add( self.output_log_filePicker, 12, wx.ALL, 5 )


		total_boxsizer1.Add( output_log_sizer, 1, wx.EXPAND, 5 )


		sbSizer62.Add( total_boxsizer1, 10, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer62, 1, wx.EXPAND, 5 )

		apply_button_boxsizer = wx.StdDialogButtonSizer()
		self.apply_button_boxsizerApply = wx.Button( self, wx.ID_APPLY )
		apply_button_boxsizer.AddButton( self.apply_button_boxsizerApply )
		apply_button_boxsizer.Realize();

		bSizer1.Add( apply_button_boxsizer, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 4, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.excel_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.excel_file_select )
		self.excel_check_button.Bind( wx.EVT_BUTTON, self.excel_check )
		self.sheet_choice.Bind( wx.EVT_CHOICE, self.excel_check_button_process )
		self.startrow_textCtrl.Bind( wx.EVT_TEXT, self.excel_check_button_process )
		self.endrow_textCtrl.Bind( wx.EVT_TEXT, self.excel_check_button_process )
		self.binary_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.binary_file_select )
		self.parse_check_button.Bind( wx.EVT_BUTTON, self.binary_check )
		self.ending_choice.Bind( wx.EVT_CHOICE, self.binary_check_button_process )
		self.parse_unit_choice.Bind( wx.EVT_CHOICE, self.binary_check_button_process )
		self.parse_number_textCtrl.Bind( wx.EVT_TEXT, self.binary_check_button_process )
		self.loop_checkBox.Bind( wx.EVT_CHECKBOX, self.loop_parse_check )
		self.output_data_format_choice.Bind( wx.EVT_CHOICE, self.output_data_format )
		self.output_choice.Bind( wx.EVT_CHOICE, self.output_choice_select )
		self.output_excel_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.output_excel_changed )
		self.output_log_filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.output_excel_changed )
		self.apply_button_boxsizerApply.Bind( wx.EVT_BUTTON, self.apply_parse_function )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def excel_file_select( self, event ):
		event.Skip()

	def excel_check( self, event ):
		event.Skip()

	def excel_check_button_process( self, event ):
		event.Skip()



	def binary_file_select( self, event ):
		event.Skip()

	def binary_check( self, event ):
		event.Skip()

	def binary_check_button_process( self, event ):
		event.Skip()



	def loop_parse_check( self, event ):
		event.Skip()

	def output_data_format( self, event ):
		event.Skip()

	def output_choice_select( self, event ):
		event.Skip()

	def output_excel_changed( self, event ):
		event.Skip()


	def apply_parse_function( self, event ):
		event.Skip()


