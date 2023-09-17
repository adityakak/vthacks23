import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import ContactUsForm from "./ContactUsForm";

function ContactUs() {
    return (
        <div>
            <Navbar />
            <div className="text-md text-white mt-10 w-1/3 mx-auto text-center">
                Please submit any questions that you may have and we will try to
                respond as soon as possible.
            </div>
            <ContactUsForm />
            <Footer />
        </div>
    );
}

export default ContactUs;
