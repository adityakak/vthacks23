function Background() {
  return (
    <div>
      {" "}
      <div className="relative pb-24 bg-home-bg bg-cover bg-no-repeat h-[41rem] z-[10] bg-red-800">
        <div className="absolute top-0 left-0 w-full h-full bg-black opacity-50 z-[2]" />

        {/* Centered orange rectangle */}
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-white text-7xl border-4  border-orange-500 w-[40rem] h-80 flex flex-col justify-center items-center rounded-3xl z-20">
          <div className="absolute top-[2%] left-[1%] border-white border-4 h-[96%] w-[98%] z-[20] rounded-2xl" />
          Advising Homes for dayz
        </div>
      </div>
    </div>
  );
}

export default Background;
