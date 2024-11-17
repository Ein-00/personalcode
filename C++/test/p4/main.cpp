#include <nana/gui.hpp>
#include <nana/gui/widgets/textbox.hpp>
#include <nana/gui/widgets/form.hpp>
#include <nana/gui/widgets/label.hpp>
int main()
    using namespace nana;

    // Create the form (window)
    form fm;
    fm.caption("Simple Text Editor");
	
  	label lb{fm, rectangle{10,20,100,30}};
  	lb.caption("Hello there");
  	

    // Show the form
    fm.show();

    // Start Nana's event loop
    exec();
}
