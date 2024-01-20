# Product interface: Document
class Document:
    def create(self):
        pass

# Concrete Products: Resume and Report
class Resume(Document):
    def create(self):
        print("Creating a Resume document")

class Report(Document):
    def create(self):
        print("Creating a Report document")

# Factory interface: DocumentFactory
class DocumentFactory:
    def create_document(self):
        pass

# Concrete Factories: ResumeFactory and ReportFactory
class ResumeFactory(DocumentFactory):
    def create_document(self):
        return Resume()

class ReportFactory(DocumentFactory):
    def create_document(self):
        return Report()

# Client code
if __name__ == "__main__":
    # Creating a Resume using ResumeFactory
    resume_factory = ResumeFactory()
    resume = resume_factory.create_document()
    resume.create()

    # Creating a Report using ReportFactory
    report_factory = ReportFactory()
    report = report_factory.create_document()
    report.create()
