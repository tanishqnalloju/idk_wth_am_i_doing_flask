class JobFunction():
    def __init__(self, Name, Job, Description, TComp, SComp,):
        self.Name = Name
        self.Job = Job
        self.Description = Description
        self.TComp = TComp
        self.SComp = SComp

#Sorting Functions
ms = JobFunction('Merge', 'Sort', 'desc', 'ms_tcomp.png', 'ms_ccomp.png')
bus = JobFunction('Bubble', 'Sort', 'desc', 'bs_tcomp.png', 'bs_ccomp.png')

#Searching Functions
ls = JobFunction('Linear', 'Search', 'desc', 'ls_tcomp.png', 'ls_ccomp.png')
bis = JobFunction('Binary', 'Search', 'desc', 'bs_tcomp.png', 'bs_ccomp.png')