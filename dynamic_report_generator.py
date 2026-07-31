# Define a decorator for formatting
def bold_text(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


# Define the Report class
class Report:
    # Class variable for storing templates
    templates = {}

    # Constructor to initialize the report with title and content
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add a template to the class variable
    @classmethod
    def add_template(cls, name, template_func):
        cls.templates[name] = template_func

    # Class method to retrieve a template from the class variable
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method to call a report instance with a template name
    def __call__(self, template_name):
        template_func = self.get_template(template_name)
        if template_func is not None:
            return template_func(self.title, self.content)
        return f"No template found for '{template_name}'"

    # String representation of the report
    def __str__(self):
        return f"Report Title: {self.title}\nContent: {self.content}"


# Define a simple template function
def simple_template(title, content):
    return f"Title: {title}\nContent: {content}"


# Define a fancy template function with bold formatting
@bold_text
def fancy_template(title, content):
    return f"Title: {title}\nContent: {content}"


# Main function to generate and display reports
def main():
    # Add templates to the Report class
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create a report instance
    report = Report("Monthly Report", "Sales increased this month.")

    # Generate reports with different templates
    simple_report = report("simple")
    fancy_report = report("fancy")

    # Display the reports
    print(simple_report)
    print()
    print(fancy_report)


# Run the main function
if __name__ == "__main__":
    main()
