#-------------------------------------------------------------------------------
#  
#  UI specific trait definitions.
#  
#  Written by: David C. Morrill
#  
#  Date: 02/26/2007
#  
#  (c) Copyright 2007 by Enthought, Inc.
#  
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:  
#-------------------------------------------------------------------------------

from enthought.traits.trait_types \
    import Str
    
from enthought.traits.ui.editors \
    import TitleEditor
        
#-------------------------------------------------------------------------------
#  Defines a Title trait:
#-------------------------------------------------------------------------------

Title = Str( editor = TitleEditor() )

