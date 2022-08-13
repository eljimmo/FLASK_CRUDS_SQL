
    def __init__(self, date, id, revenue, brokerage, driver, commodity, weight, pickup_date, end_date, shippers, receivers, mileage, status, notes):
            self.id= id
            self.date = date
            self.revenue = revenue
            self.brokerage = brokerage
            self.driver = driver
            self.commodity = commodity
            self.weight = weight
            self.pickup_date = pickup_date 
            self.end_date = end_date
            self.shippers = shippers
            self.receivers = receivers
            self.mileage = mileage
            self.status = status
            self.notes = notes


            
    def __str__(self):
        return '{} by {} for {}'.format(self.id, self.brokerage, self.revenue)




class brokerage(models.Model):

    __tablename__='brokerages'

    brokerageID = models.AutoField(primary_key=True)
    brokerageName = models.CharField(max_length=500)
    brokerageAddress = models.CharField(max_length=500)
    brokeragePODEmail = models.CharField(max_length=500, null=True)
    brokerageDateAdded = models.DateTimeField()

    def __str__(self):
        return 'Brokerage: {} Address: {} ID: {} Date Added: {}'.format(self.brokerageName, self.brokerageAddress, self.brokerageID, self.brokerageDateAdded)
        

class Driver(models.Model):

    __tablename__='Drivers'
    
    DriverID = models.AutoField(primary_key=True)
    DriverName = models.CharField(max_length=500)
    DriverCDLNumber = models.CharField(max_length=500)
    LicenceExpiration = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    LicenseRestrictions = models.CharField(max_length=500)
    PhotoFileName = models.CharField(max_length=500)

    def __init__(self, DriverId, DriverName, DriverCDLNumber, LicenseExpiration, DateOfJoining, LicenseRestrictions, PhotoFileName):
        
        self.DriverID = DriverId
        self.DriverName = DriverName
        self.DriverCDLNumber = DriverCDLNumber
        self.LicenceExpiration = LicenseExpiration
        self.DateOfJoining = DateOfJoining
        self.LicenseRestrictions = LicenseRestrictions
        self.PhotoFileName = PhotoFileName

    def __str__(self):
        return 'Driver: {} CDL: {} License Restriction: {} Photo: {} Date of Joining: {} License Date Expiration {}'.format(self.DriverName, self.DriverCDLNumber, self.LicenseRestrictions, self.PhotoFileName, self.DateOfJoining, self.LicenceExpiration)



class shippers(models.Model):

    __tablename__='shippers'

    Address = models.CharField(max_length=500)
    
    def __init__(self, Address):

        self.Address = Address

class receivers(models.Model):

    __tablename__='receivers'

    Address = models.CharField(max_length=500)
    
    def __init__(self, Address):

        self.Address = Address
