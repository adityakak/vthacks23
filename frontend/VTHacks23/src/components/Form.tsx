import { useState } from "react";
import { useForm } from 'react-hook-form';
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
    <div className="relative pb-24 bg-home-bg bg-cover bg-no-repeat h-[41rem] z-[-1] ">
                <div className="absolute top-0 left-0 w-full h-full bg-black opacity-40" />
                {isAboveMediumScreens && (
                    <div className="relative pt-56 w-[40rem] ml-32 mx-auto text-white ">
                        <div className="relative text-white bg-wise-light-blue p-4 rounded-2xl ">
                            <div className="absolute top-1 left-1 bg-wise-blue h-full w-full z-[-2] rounded-2xl" />
                            <div className="absolute top-2 left-2 bg-wise-red h-full w-full z-[-3] rounded-2xl" />
                            <div className="absolute top-3 left-3 bg-white h-full w-full z-[-4] rounded-2xl" />
                            <div className="text-8xl font-bold">
                                Year in Wise
                            </div>
                            <div className="mt-12 text-2xl font-normal">
                                This is Where it all Begins
                            </div>
                        </div>
                    </div>
                )}
            </div>
    <form className="flex flex-col justify-center items-center h-full"
      onSubmit={handleSendHome}
    >  
        <input className="mb-2 rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto w-[800px]"
            value={address}
            type="text"
            placeholder="Address Line 1"
            {...register('address', {
              required: true,
              maxLength: 100,
          })}
            onChange={(
              e: React.ChangeEvent<HTMLInputElement>
          ) => {
              setAddress(e.target.value);
          }}
        />
       {errors.address && (
                            <p className=" text-primary-500 mb-2">
                                {errors.address.type === 'required' &&
                                    'This field is required.'}
                                {errors.address.type === 'maxLength' &&
                                    'Max Length is 100 characters.'}
                            </p>
                        )
        }

        <div className="md:grid grid-cols-3 w-[800px] gap-2">
          <div>
          <input className="mb-2 w-full rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto"
            value={city}
            type="text"
            placeholder="City"
            {...register('city', {
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
                                {errors.city.type === 'required' &&
                                    'This field is required.'}
                                {errors.city.type === 'maxLength' &&
                                    'Max Length is 100 characters.'}
                            </p>
                        )
        }
          </div>
          <div>
          <select className="mb-2 w-full rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto"
            value={state}
            placeholder="State"
            {...register('state', {
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
                                <option
                                    value={state}
                                    key={state}
                                >
                                    {state}
                                </option>
                            ))}
          </select>
       {errors.state && (
                            <p className=" text-primary-500">
                                {errors.state.type === 'required' &&
                                    'This field is required.'}
                                {errors.state.type === 'maxLength' &&
                                    'Max Length is 100 characters.'}
                            </p>
                        )
        }
          </div>

          <div>
          <input className="mb-2 w-full rounded-lg bg-blue-400 px-5 py-3 placeholder-white text-white mx-auto"
            value={zip}
            type="text"
            placeholder="Zip Code"
            {...register('zip', {
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
                                {errors.zip.type === 'required' &&
                                    'This field is required.'}
                                {errors.zip.type === 'maxLength' &&
                                    'Max Length is 100 characters.'}
                            </p>
                        )
        }
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
  )
}

export default Form