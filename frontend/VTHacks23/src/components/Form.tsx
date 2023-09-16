import { useState } from "react";
import { useForm } from "react-hook-form";
import { states } from "../shared/states";

function Form() {
    const [address, setAddress] = useState<string>();
    const [city, setCity] = useState<string>();
    const [state, setState] = useState<string>();
    const [zip, setZip] = useState<string>();
    const {
        register,
        trigger,
        formState: { errors },
    } = useForm();

    async function handleSendHome(e: React.FormEvent) {
        e.preventDefault();
        const isValid = await trigger();
    }
    return (
        <>
            <div className="group">
                <div className="flex justify-center my-10">
                    <span className="text-white text-4xl bg-left-bottom bg-gradient-to-r from-orange-400 to-orange-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out italic">
                        Enter your address below
                    </span>
                </div>

                <div className="mx-auto border-white w-5 h-5  my-6 border-t-2 border-r-2 transform rotate-[135deg] transition-all duration-500 group-hover:translate-y-6" />
            </div>

            <form
                className="relative flex flex-col justify-center items-center h-full py-24"
                onSubmit={handleSendHome}
            >
                <input
                    className="mb-2 rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto w-[800px]"
                    value={address}
                    type="text"
                    placeholder="Address Line 1"
                    {...register("address", {
                        required: true,
                        maxLength: 100,
                    })}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                        setAddress(e.target.value);
                    }}
                />
                {errors.address && (
                    <p className=" text-primary-500 mb-2">
                        {errors.address.type === "required" &&
                            "This field is required."}
                        {errors.address.type === "maxLength" &&
                            "Max Length is 100 characters."}
                    </p>
                )}

                <div className="md:grid grid-cols-3 w-[800px] gap-2">
                    <div>
                        <input
                            className="mb-2 w-full rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto"
                            value={city}
                            type="text"
                            placeholder="City"
                            {...register("city", {
                                required: true,
                                maxLength: 100,
                            })}
                            onChange={(
                                e: React.ChangeEvent<HTMLInputElement>
                            ) => {
                                setCity(e.target.value);
                            }}
                        />
                        {errors.city && (
                            <p className=" text-primary-500">
                                {errors.city.type === "required" &&
                                    "This field is required."}
                                {errors.city.type === "maxLength" &&
                                    "Max Length is 100 characters."}
                            </p>
                        )}
                    </div>
                    <div>
                        <select
                            className="mb-2 w-full rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto border-r-8 border-transparent"
                            value={state}
                            placeholder="State"
                            {...register("state", {
                                required: true,
                            })}
                            onChange={(
                                e: React.ChangeEvent<HTMLSelectElement>
                            ) => {
                                setState(e.target.value);
                            }}
                        >
                            <option value=""> State </option>
                            {states?.map((state) => (
                                <option value={state} key={state}>
                                    {state}
                                </option>
                            ))}
                        </select>
                        {errors.state && (
                            <p className=" text-primary-500">
                                {errors.state.type === "required" &&
                                    "This field is required."}
                                {errors.state.type === "maxLength" &&
                                    "Max Length is 100 characters."}
                            </p>
                        )}
                    </div>

                    <div>
                        <input
                            className="mb-2 w-full rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto"
                            value={zip}
                            type="text"
                            placeholder="Zip Code"
                            {...register("zip", {
                                required: true,
                                maxLength: 100,
                            })}
                            onChange={(
                                e: React.ChangeEvent<HTMLInputElement>
                            ) => {
                                setZip(e.target.value);
                            }}
                        />
                        {errors.zip && (
                            <p className=" text-primary-500">
                                {errors.zip.type === "required" &&
                                    "This field is required."}
                                {errors.zip.type === "maxLength" &&
                                    "Max Length is 100 characters."}
                            </p>
                        )}
                    </div>
                </div>

                <button
                    type="submit"
                    className="md:w-64 sm:w-full xs:w-full mt-20 bg-white hover:text-white border-black border-2 p-3 rounded-md hover:bg-blue-600 transition-all duration-500"
                >
                    Submit
                </button>
            </form>
        </>
    );
}

export default Form;
