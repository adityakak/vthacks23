type Props = {
    placeNumber: number;
    imageLink: string;
    address: string;
    homesLink: string;
};

function Houses({ placeNumber, imageLink, address, homesLink }: Props) {
    return (
        <div className="relative w-[400px] h-[400px] bg-white text-orange-600 text-2xl flex justify-evenly items-center text-center flex-col rounded-2xl mb-10">
            <div className="absolute top-0 left-0 ml-4 mt-6 w-12 h-16 rounded-full border-4 border-orange-600 flex items-center justify-center">
                {placeNumber}
            </div>
           <a href={homesLink}> <img alt="house" src={imageLink} width={250} /></a> 

            <div className="px-2">
            {address}
            </div>
        </div>
    );
}

export default Houses;
