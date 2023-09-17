/* eslint-disable @typescript-eslint/no-unused-vars */
import { useForm } from "react-hook-form";
import { motion } from "framer-motion";
import { useState } from "react";

function ContactUsForm() {
    const inputStyles = `mt-5 w-full rounded-lg bg-gray-200 px-5 py-3 placeholder-orange-600 border-orange-600 border-2 text-orange-600`;
    /* Destructuring syntax so that we can reference the register, trigger, formState(errors) object as just register, trigger and errors rather then useForm.register making it simpiler [cleaner code] */
    /* register -> Registers form inputs, so the form can track the inputted values along with validation rules */
    /* trigger -> Manually triggers validation for all registered fields so you can perform validation before submitting */
    /* errors -> contains info about validation errors that might have occurred for a registered field so we can display such error messages in an easy way */
    const {
        register,
        trigger,
        formState: { errors },
    } = useForm();

    const [name, setName] = useState<string>("");
    const [email, setEmail] = useState<string>("");
    const [message, setMessage] = useState<string>("");

    /* aync because we want to await for async functions to complete before we start execution of our code again */
    /* e is the eventObject and has its own type but for time's sake, we just put any */
    /* Once the validation checks are complete (await trigger) then isValid stores a boolean val of that execution */
    /* if it isn't valid, then we prevent the default behavior, which is the form being submitted */

    const onSubmit = async (e: React.FormEvent) => {
        const isValid = await trigger();
        if (!isValid) {
            e.preventDefault();
        }
    };

    const formSubmitKey: string | undefined = import.meta.env
        .VITE_REACT_APP_FORM_SUBMIT_KEY;

    return (
        <motion.div
            className="mt-10 mx-auto w-2/5 md:mt-0 "
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.5 }}
            transition={{ duration: 0.5 }}
            variants={{
                hidden: { opacity: 0, y: 50 },
                visible: { opacity: 1, y: 0 },
            }}
        >
            {/* REACT HOOK FORM */}
            {/* target (_blank) specifies that we open the response in a new tab upon form submission */}
            {/* onSubmit calls our own onSubmit function that was created */}
            {/* action -> Using the formsubmit service, when the data is submitted, it will submitted to the specified email address [to prevent spamming, formSubmit provides its own url for your email */}
            {/* Since we are sending data, we will be using the post method [commonly used for form submission] */}
            <form
                target="_blank"
                onSubmit={onSubmit}
                action={`https://formsubmit.co/${formSubmitKey}`}
                method="POST"
            >
                {/* ...register (takes that input and places it underneath the name section so that we can access if there are any errors ) */}
                {/* It is followed by the specific validation checks (required -> true and maxlength of 100 characters) */}
                <input
                    className={inputStyles}
                    type="text"
                    placeholder="NAME"
                    {...register("name", {
                        required: true,
                        maxLength: 100,
                    })}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                        setName(e.target.value);
                    }}
                />
                {/* if there are any errors for the name attribute that was just inputted then check to see the type and display the appropriate text */}
                {errors.name && (
                    <p className="mt-1 text-primary-500">
                        {errors.name.type === "required" &&
                            "This field is required."}
                        {errors.name.type === "maxLength" &&
                            "Max Length is 100 characters."}
                    </p>
                )}

                {/* ...register (takes that input and places it underneath the name section so that we can access if there are any errors ) */}
                {/* It is followed by the specific validation checks (required -> true and has to follow a specific pattern for email ) */}
                <input
                    className={inputStyles}
                    type="text"
                    placeholder="EMAIL"
                    {...register("email", {
                        required: true,
                        pattern: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                    })}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                        setEmail(e.target.value);
                    }}
                />
                {/* if there are any errors for the name attribute that was just inputted then check to see the type and display the appropriate text */}
                {errors.email && (
                    <p className="mt-1 text-primary-500">
                        {errors.email.type === "required" &&
                            "This field is required."}
                        {errors.email.type === "pattern" &&
                            "Please enter a valid email address."}
                    </p>
                )}

                {/* ...register (takes that input and places it underneath the name section so that we can access if there are any errors ) */}
                {/* It is followed by the specific validation checks (required -> true and maxlength of 2000 charactes) */}
                {/* Make the messages area a textArea to make that section larger than the rest [takes in number of rows and cols instead of a type like for input] */}
                <textarea
                    className={inputStyles}
                    rows={8}
                    cols={50}
                    placeholder="MESSAGE"
                    {...register("message", {
                        required: true,
                        maxLength: 2000,
                    })}
                    onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => {
                        setMessage(e.target.value);
                    }}
                />
                {/* if there are any errors for the name attribute that was just inputted then check to see the type and display the appropriate text */}
                {errors.message && (
                    <p className="mt-1 text-primary-500">
                        {errors.message.type === "required" &&
                            "This field is required."}
                        {errors.message.type === "maxLength" &&
                            "Max Length is 2000 characters."}
                    </p>
                )}

                <div className="flex justify-center">
                    <button
                        type="submit"
                        className="mt-5 mb-12 rounded-lg border-orange-500 border-2 bg-blue-100 px-20 py-3 transition duration-500 hover:text-orange-600"
                    >
                        SUBMIT
                    </button>
                </div>
            </form>
        </motion.div>
    );
}

export default ContactUsForm;
