type Props = {
    name: string;
    image: string;
};

function DeveloperCard({ name, image }: Props) {
    return (
        <div className="bg-orange-600 h-64 w-96 flex border-2 ">
            <div className="w-2/5 flex justify-center items-center">
                <img
                    className="h-32 w-32 rounded-full border-2"
                    src={image}
                    alt="advisor img"
                />
            </div>
            <div className="w-3/5 flex items-center text-white">
                <div className="ml-6 ">
                    <div className="text-xl font-medium">{name}</div>
                </div>
            </div>
        </div>
    );
}

export default DeveloperCard;
