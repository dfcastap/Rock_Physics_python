# My Pyton Logs Module
#

import Tkinter as tk

"""
Class: Log( ValueID="",ValueUnit="",DepthUnit="",Start=0.0,End=99999.0,Inc=1.0,NumVal=0,
            Null=-999.25,MD=[],TVD=[],TVDss=[],Value=[],Value1Unit="",Value1=[],
            Value2Unit="",Value2=[],Value3Unit="",Value3=[],Value4Unit="",Value4=[] )

An instance of a Log does not require any input. This object is ment to hold information from a single well log.
Currently, this object does not have all the attributes that would be in the header of a well log. Potentially
this might be added at a later date or another class would be defined to hold this information.
"""
class Log:
    def __init__(self,ValueID="",ValueUnit="",DepthUnit="",Start=0.0,End=99999.0,Inc=1.0,NumVal=0,
                 Null=-999.25,MD=[],TVD=[],TVDss=[],Value=[],Value1Unit="",Value1=[],
                 Value2Unit="",Value2=[],Value3Unit="",Value3=[],Value4Unit="",Value4=[]):
        """
        Logs takes up to 19 arguements none of which need to be specified. This class is ment to
		hold description and values of a typical borehole log. Currently I see this as just a holder
		of the log values with bare bones description of these values. For more detailed description of 
		the log and associated logs in this well, as would be provided by the curve description portion
		of a LAS file, use the class 'CurvesInfoLAS' defined in this module.
        """
        self.ValueID = ValueID              # The main type of measured log Value
        self.ValueUnit = ValueUnit          # The units associated with the main type of Value
        self.DepthUnit = DepthUnit          # The units the measured depth is given in
        self.Start = Start                  # The shallowest depth with log Value including nulls
        self.End = End                      # The deepest depth with log Value including nulls
        self.Inc = Inc                      # The increment or depth steps for Value
        self.NumVal = NumVal                # The total number of Values
        self.Null = Null                    # The value used to represent a null value
        self.MD = MD                        # The measured depth array associated with Value
        self.TVD = TVD                      # The corresponding true vertical depth array
        self.TVDss = TVDss                  # The corresponding true vertical depth subsea
        self.Value = Value                  # The primary measured Value array
        self.Value1Unit = Value1Unit        # The secondary value's units if needed
        self.Value1 = Value1                # Secondary Value array
        self.Value2Unit = Value2Unit        # The tertiary value's units if needed
        self.Value2 = Value2                # Tertiary Value array
        self.Value3Unit = Value3Unit        # The quaternary value's units if needed
        self.Value3 = Value3                # quaternary Value array
        self.Value4Unit = Value4Unit        # The quinary value's units if needed
        self.Value4 = Value4                # quinary Value array
    
    def setValueID(self, ValueID):
        """
        Takes one argument, the type of log this will be
        """
        self.ValueID = ValueID
    
    def setValueUnit(self, ValueUnit):
        """
        Takes one argument, the Units of the Value of this log
        """
        self.ValueUnit = ValueUnit
    
    def setDepthUnit(self, DepthUnit):
        """
        Takes one argument, the Units of the Value of this log
        """
        self.DepthUnit = DepthUnit
    
    def setStart(self, Start):
        """
        Takes one argument, the Starting depth of the Value of this log
        """
        self.Start = Start
    
    def setEnd(self, End):
        """
        Takes one argument, the Ending depth of the Value of this log
        """
        self.End = End
    
    def setInc(self, Inc):
        """
        Takes one argument, the Incremental depth between the Value of this log
        """
        self.Inc = Inc
    
    def setNumVal(self, NumVal):
        """
        Takes one argument, the Incremental depth between the Value of this log
        """
        self.NumVal = NumVal
    
    def setNull(self, Null):
        """
        Takes one argument, the Null value used if no actual log value exists
        """
        self.Null = Null
    
    def setMD(self, MD):
        """
        Takes one argument, the measured depth array of this log
        """
        self.MD = MD
    
    def setTVD(self, TVD):
        """
        Takes one argument, the the true vertical depth array of this log
        """
        self.TVD = TVD
    
    def setTVDss(self, TVDss):
        """
        Takes one argument, the the true vertical depth subsea array of this log
        """
        self.TVDss = TVDss
    
    def setValue(self, Value):
        """
        Takes one argument, the primary value array of this log,
        Most logs will only have one value array and it should be placed here.
        The value array contains the actual measured Value from the logging process.
        """
        self.Value = Value
    
    def setValue1Unit(self, ValueUnit):
        """
        Takes one argument, the Units of the Value of this log
        """
        self.Value1Unit = Value1Unit
    
    def setValue1(self, Value1):
        """
        Takes one argument, the secondary value array of this log
        """
        self.Value1 = Value1
    
    def setValue2Unit(self, ValueUnit):
        """
        Takes one argument, the Units of the Value of this log
        """
        self.Value2Unit = Value2Unit
    
    def setValue2(self, Value2):
        """
        Takes one argument, the tertiary value array of this log
        """
        self.Value2 = Value2
    
    def setValue3Unit(self, ValueUnit):
        """
        Takes one argument, the Units of the Value of this log
        """
        self.Value3Unit = Value3Unit
    
    def setValue3(self, Value3):
        """
        Takes one argument, the quaternary value array of this log
        """
        self.Value3 = Value3
    
    def setValue4Unit(self, ValueUnit):
        """
        Takes one argument, the Units of the Value of this log
        """
        self.Value4Unit = Value4Unit
    
    def setValue4(self, Value4):
        """
        Takes one argument, the quinary value array of this log
        """
        self.Value4 = Value4


class BunchOfLogs:
	"""

	This class is ment to be a container for a collection of logs, which can easily accessed for further processing.
	Not a lot of extranious information about the logs is contained here only what comes with the 'Log' object.
	
	Current avaialable function assoicated with this object:
	
	appendALog( newLog, newLogId )	    inserts a new Log object into the BunchOfLogs object
                                            this should be invoked with a new log object and a new ID
                                            If no new ID is specified it will default to the log type
                                            and if no new Log is specified an empty Log will be appended

	"""	
	def __init__( self, myLogLabel=[], logType=[] , theLog=[Log()], numLogs=0, choiceNumber=-999 ):

		self.myLogLabel = myLogLabel					# An arbitrary ID for a log, for example its well name
		self.logType = logType							# The log type associated with corresponding ID label
		self.theLog = theLog							# The values and other information of corresponding log
		self.numLogs = numLogs							# Number of logs in this bunch of Logs
		self.choiceNumber = choiceNumber				# Variable to hold the number of a particular log

	def setmyLogLabel( self, myLogLabel ):
		"""
		Takes one list, the list of user defined ID's for the associated logs.
		"""
		self.myLogLabel = myLogLabel

	def setlogType( self, logType ):
		"""
		Takes one list, the list of log types corresponding to defined ID's list.
		"""
		self.logType = logType

	def settheLog( self, theLog ):
		"""
		Takes a list of "Log" objects, containing values of the logs and additonal information 
		that can be found in class "Log" in "MyLogsMod" module.
		"""
		self.theLog = theLog

	def setnumLogs( self, numLogs ):
		"""
		Takes one argument, the number of logs in this bunch of logs.
		"""
		self.numLogs = numLogs

	def setchoiceNumber( self, choiceNumber ):
		"""
		An integer variable usually set to a particular log number for further computation.
		If there is no choices made or available then the value is generally set to -999 to 
		indicate this situation. The default value is -999.
		"""
		self.setchoiceNumber = choiceNumber
	
	def appendALog( self, newLog = Log(), newLogId = "" ):
		"""
		Appends a new Log object to the BunchOfLogs object
		"""
		print "+-----------------------------------------------------+"
		print "|                                                     |"
		print "|           Entering Append a 'Log' Object            |"
		print "|           to a 'BunchOfLogs' Object function        |"
		print "|                                                     |"
		print "+-----------------------------------------------------+"

		if self.newLogId  == "":
			self.newLogId  = self.newLog.ValueID

		logsAreUs.numLogs = logsAreUs.numLogs + 1
		logsAreUs.myLogLabel.append( self.newLogId )
		logsAreUs.logType.append( self.newLog.ValueID)
		logsAreUs.theLog.insert( int(logsAreUs.numLogs - 1), self.newLog )

		myStdErrorMessage( "Append Log Report", 
							"Number of logs: " + str(logsAreUs.numLogs) + 
							"\n Appended log ID: " + str(logsAreUs.myLogLabel) + 
							"\n Appended log Type: " + str(logsAreUs.logType))

		print ""
		print "New number of Logs    : " + str( logsAreUs.numLogs )
		print "New Log Identifier    : " + str( logsAreUs.myLogLabel[ logsAreUs.numLogs - 1 ] )
		print "Type of log appended  : " + str( logsAreUs.logType[ logsAreUs.numLogs - 1 ] )
		print "Units for appended log: " + str( self.newLog.ValueUnit )
		print "Units after append    : " + str( logsAreUs.theLog[ logsAreUs.numLogs -1].ValueUnit )


def Read1LogFromLasFileNoWrap(LasFile,LogName):
    f = open(LasFile,"r")
    aLog = Log()
    count = -1
    flag1 = 0
    DepthCol = -111
    LogCol = -111
    DepthName = "DEPT"
    ValueStore = []
    DepthStore = []
    for line in f:
        
        if line[0] != "#":
            
            if line.strip().split()[0] == "~Curve" or flag1 == 1:
                count = count + 1
                flag1 = 1
                
                if line.strip().split()[0] == LogName:
                    LogCol = count
                    aLog.setValueID( line.split()[0] )
                    aLog.setValueUnit( line.split()[1].lstrip(".") )
                
                if line.strip().split()[0] == DepthName:
                    DepthCol = count
                    aLog.setDepthUnit( line.split()[1].lstrip(".") )
                
                if line.strip().split()[0] == "~Parameter" and LogCol == -111:
                    print "/n No log in LAS file contains your requested log type: " + str(LogName)
                    break
                
                elif line.strip().split()[0] == "~Parameter" and LogCol != -111:
                    flag1 = 0
                    count = -1
            
            if line.strip().split()[0] == "~Ascii" or flag1 == 2:
                count = count + 1
                if flag1 == 2:
                    ValueStore.append( float( line.split()[ LogCol-1 ] ) )
                    DepthStore.append( float( line.split()[DepthCol-1] ) )
                
                flag1 = 2

    aLog.setValue( ValueStore )
    aLog.setMD( DepthStore )
    aLog.setStart( DepthStore[0] )
    aLog.setEnd( DepthStore[count-1] )
    aLog.setInc( aLog.MD[1]-aLog.MD[0] )
    aLog.setNumVal( len(ValueStore) )

    f.close()
    
    return aLog

class CurvesInfoLAS:
    """
    This class is ment to contain information found in the (curve information block) section
    of a LAS file
    """
    def __init__( self, logMnemonic=[], logUnit=[], logDescription=[], numCurves=0 ):
        """
        CurvesFromLAS takes 4 arguments that need not be specified to create an object
        """
        
        self.logMnemonic = logMnemonic              # The associated mnemonic for type of log curve in LAS file
        self.logUnit = logUnit                      # The units associated with corresponding mnemonic
        self.logDescription = logDescription        # The description of the log associted with the corresponding mnemonic
        self.numCurves = numCurves                  # The units associated with corresponding mnemonic
        
        def setlogMnemonic( self, logMnemonic ):
            """
            Takes a list of arguments, representing the log mnemoics found in a LAS file
            """
            self.logMnemonic = logMnemonic
        def setlogUnit( self, logUnit ):
            """
            Takes a list of arguments, representing the units found in a LAS file
            """
            self.logUnit = logUnit
        
        def setlogDescription( self, logDescription ):
            """
            Takes a list of arguments, with description of the logs found in a LAS file
            """
            self.logDescription = logDescription
        
        def setnumCurves( self, numCurves ):
            """
            Takes one argument, the number of curves found in LAS file
            """
            self.LognumCurves = numCurves



def ReadLogTypesFromLasFile(LasFile):
    """
    This function reads the curve information block in a LAS file
    and outputs the associated log mnemonic, log units, log description
    and the determined number of logs in the file into a CurvesInfoLAS object.
    """
    f = open(LasFile,"r")
    CurveNamesEtc = CurvesInfoLAS()
    count = -1
    flag1 = 0
    
    for line in f:
        
        if line[0] != "#":
            
            if line.split()[0] == "~Curve" or flag1 == 1:
                count = count + 1

                if line.split()[0] == "~Parameter" and flag1 != 2:
                    flag1 = 2
                    CurveNamesEtc.numCurves = count - 1
                
                elif flag1 == 1:
                    CurveNamesEtc.logMnemonic.append(line.split()[0])
                    CurveNamesEtc.logUnit.append(line.split()[1].strip("."))
                    a = line.split()
                    del( a[0] )
                    del( a[0] )
                    del( a[0] )
                    b = ''
                    for i in range(len(a)):
                        b = b + str(a[i]) + ' '

                    CurveNamesEtc.logDescription.append(b.rstrip())

                else:
                    flag1 = 1

    f.close()
    
    return CurveNamesEtc

class getALogFromBunchOfLogs:
	"""
	This allow the selection of a log from a bunch of logs and sets up variables
	to be used in other process. The relevant variables useful from this class would be:
	
			self.logId	---------> The log ID as read from aBunchOfLogs
			self.logType	---------> The log type as read from aBunchOfLogs
			self.logUnit	---------> The log unit as read from the choosen log within aBunchOfLogs
			self.logValues 	---------> Array containing the actual log values
			self.logNumber	---------> The position number of choosen log within aBunchOfLogs
			
	"""
	
	def __init__( self, parent = tk.Tk(), aBunchOfLogs = BunchOfLogs() ):
		
		self.parent = parent			# tk window from calling function
		self.aBunchOfLogs = aBunchOfLogs	# BunchOfLogs object from calling function
		
		self.logId = "None"			# ID of chosen log
		self.logType = "None"			# Log type of chosen log
		self.logUnit = "None"			# Unit of chosen log
		self.logValues = []			# Actual values list of chosen log
		self.logNumber = -999			# Index of chosen log within the BunchOfLogs object
		
		if self.aBunchOfLogs.numLogs == 0:
			
			self.logId = "None"
			self.logType = "None"
			self.logUnit = "None"
			self.logValues = []
			self.logNumber = -999
		
		else:
			
			self.brother = tk.Toplevel( self.parent )
			self.brother.wm_title( "Select a log function" )
			
			self.logPosition = tk.IntVar( self.brother )
			self.logPosition.set( -999 )
			
			self.rowCounter = 0 #===================================================================
			
			self.pickLogLabel = tk.Label( self.brother, 
									text = "Pick a log from the list below.", 
									font = ("Comic Sans MS",16), 
									fg = "Blue" )
			self.pickLogLabel.grid( row = self.rowCounter, columnspan = 3, padx = 20, pady = 10 )
			
			self.rowCounter += 1 #---------------------------------------------------------
			
			self.idLabel = tk.Label( self.brother, 
									text = "Log ID", 
									font = ("Comic Sans MS",14), 
									fg = "Green" )
			self.idLabel.grid( row = self.rowCounter, column = 0, padx = 30, pady = 5 )
			
			self.typeLabel = tk.Label( self.brother, 
									text = "Log Type", 
									font = ("Comic Sans MS",14), 
									fg = "Green" )
			self.typeLabel.grid( row = self.rowCounter, column = 1, padx = 20, pady = 5 )
			
			self.unitLabel = tk.Label( self.brother, 
									text = "Log Unit", 
									font = ("Comic Sans MS",14), 
									fg = "Green" )
			self.unitLabel.grid( row = self.rowCounter, column = 2, padx = 20, pady = 5 )
			
			self.rowCounter += 1 #---------------------------------------------------------
			
			for i in range( self.aBunchOfLogs.numLogs):
				
				self.LogIdLabel = tk.Label( self.brother, 
									text = str( self.aBunchOfLogs.myLogLabel[i] ), 
									font = ("Comic Sans MS",14), 
									fg = "Black" )
				self.LogIdLabel.grid( row = self.rowCounter, column = 0, padx = 30 )
				
				self.logTypeRadioButton = tk.Radiobutton( self.brother, 
									text = str( self.aBunchOfLogs.logType[i] ),
									variable = self.logPosition,
									value = int(i), 
									font = ("Comic Sans MS",14), 
									fg = "Black", 
									command = self.setGetALogVariables )
				self.logTypeRadioButton.grid( row = self.rowCounter, column = 1, sticky = tk.W, padx = 20 )
				
				self.logUnitLabel = tk.Label( self.brother, 
									text = str( self.aBunchOfLogs.theLog[i].ValueUnit ), 
									font = ("Comic Sans MS",14), 
									fg = "Black" )
				self.logUnitLabel.grid( row = self.rowCounter, column = 2, padx = 20 )
				
				self.rowCounter += 1 #---------------------------------------------------------
				
			self.exitButton = tk.Button( self.brother,
									text = "Exit", 
									font = ("Comic Sans MS",14), 
									fg = "Red", 
									command = self.brother.destroy )
			self.exitButton.grid( row = self.rowCounter, column = 1, sticky = tk.E+tk.W, padx = 20, pady = 10 )
			
			self.brother.mainloop()
		
		
	def setGetALogVariables( self ):
		"""
		Set class variables associated with your log choice then close choice window.
		"""
		self.logId = str( self.aBunchOfLogs.myLogLabel[self.logPosition.get()] )
		self.logType = str( self.aBunchOfLogs.logType[self.logPosition.get()] )
		self.logUnit = str( self.aBunchOfLogs.theLog[self.logPosition.get()].ValueUnit )
		self.logValues = self.aBunchOfLogs.theLog[self.logPosition.get()].Value
		self.logNumber = self.logPosition.get()
		
		print "\n You have choosen log number (" + str(self.logNumber) + ")\n"
		print "      Log ID   : " + self.logId
		print "      Log Type : " + self.logType
		print "      Log Unit : " + self.logUnit + "\n"
		
		self.brother.destroy()
		# self.brother.quit()

def readOneRowFromAscii( fileName, rowNumber ):
    """
    Read a single row from an ascii file and output an list with
    each element of the array being space separated strings from
    your specified row.

    """
    f = open(fileName,'r')
    count = 0
    for line in f:
        count += 1
        if count == rowNumber:
            output = line.strip().split()
            f.close()
            return output

    print ""
    print "**** Error from readOneRowFromAscii ****"
    print ""
    print "      Row number was not reached your file maybe too short"
    print ""
    return

    
	

