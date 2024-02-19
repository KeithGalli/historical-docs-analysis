inputs = [
    "John James agrees to pay $50/month to RJ Hampshire for work on the Farm",
    "Elizabeth James will pay $30 per month to Levi Rodgers for Gardening",
    "Johnson Ollaman will pay $1.25 per day to both John Smith and Jane Smith for teaching the children of the community",
    "Claire Daniels charges $50 weekly to local community members for cooking classes, emphasizing the joy of healthy eating.",
    "Marcus Wellby commits to donating $500 annually to the Green Earth Foundation for environmental conservation efforts.",
    "Dr. Helena Russell charges $100 per hour for providing guidance and support to medical students, aiming to enhance their clinical skills and knowledge.",
    "Keith Galli charges $0 to watch his YouTube content; the least you could do is smash that like button and subscribe, hehehe xD",
    "The local sports club agrees to pay $75 each to coaches Sarah Miller, Danny Glover, Alex Reed, and Jamie Fox for conducting a weekend sports clinic.",
    """This Agreement made this 14th day of August A.D. 1865, by and between F.R.J. Terry of the county of Copiah and State of Mississippi of the first part, and the person hereinafter named and undersigned, Freedmen of the second part [[?]] That for the purpose of working in the [[?]] known as Beagley's [[?]] Yard in the county aforesaid for two months commencing on the 14th day of August 1865 and terminating on the 14th day of October 1865. The said F.R.J. Terry party of the first part, in consideration of the [[?]] and conditions hereinafter mentioned on the part of the party of the second part agrees to pay said laborer "10" ten dollars per month and furnish free of charge clothing and good of good quality and sufficient quantity, good and sufficient quarters, and kind and humane treatment. And it is further agreed that in case the said F.R.J. Terry shall fail, neglect, or refuse to fulfill any of the obligations assumed by him, he shall besides the legal recourse left to the party aggrieved render this contract liable to amendment by the Provost Marshal of Freedmen. And it is agreed on the part of the party of second part that he will well and faithfully perform such labor as the said F.R.J. Terry may require of him for the time aforesaid, nor exceeding ten hours per day in summer and nine hours in winter. And in case the said laborer shall absent himself from or refuse to perform the labor herein promised, he shall loose the time and be punished as such manner as the Provost Marshal shall deem propper.""",
]

outputs = [
    [{"payer": "John James", "recipient": "RJ Hampshire", "amount": 50, "pay frequency": "monthly", "description": "farming"}],
    [{"payer": "Elizabeth James", "recipient": "Levi Rodgers", "amount": 30, "pay frequency": "monthly", "description": "gardening"}],
    [{"payer": "Johnson Ollaman", "recipient": "John Smith", "amount": 1.25, "pay frequency": "daily", "description": "teaching the children of the community"}, {"payer": "Johnson Ollaman", "recipient": "Jane Smith", "amount": 1.25, "pay frequency": "daily", "description": "teaching the children of the community"}],
    [{"payer": "Claire Daniels", "recipient": "Local community members", "amount": 50, "pay frequency": "weekly", "description": "cooking classes"}],
    [{"payer": "Marcus Wellby", "recipient": "Green Earth Foundation", "amount": 500, "pay frequency": "yearly", "description": "donation for environmental conservation"}],
    [{"payer": "Dr. Helena Russell", "recipient": "Medical students", "amount": 100, "pay frequency": "hourly", "description": "mentorship and clinical skill enhancement"}],
    [{"payer": None, "recipient": "Keith Galli", "amount": 0, "pay frequency": None, "description": "YouTube content"}],
    [{"payer": "The local sports club", "recipient": "Sarah Miller", "amount": 75, "pay frequency": "one-time", "description": "weekend sports clinic"},
     {"payer": "The local sports club", "recipient": "Danny Glover", "amount": 75, "pay frequency": "one-time", "description": "weekend sports clinic"},
     {"payer": "The local sports club", "recipient": "Alex Reed", "amount": 75, "pay frequency": "one-time", "description": "weekend sports clinic"},
     {"payer": "The local sports club", "recipient": "Jamie Fox", "amount": 75, "pay frequency": "one-time", "description": "weekend sports clinic"}],
    [{"payer": "F.R.J. Terry", "payee": "Freedmen", "amount":10, "pay frequency": "monthly", "description": "working in the yard"}],
]
