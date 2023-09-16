import { useState, useEffect } from 'react';
/* Import the react hooks from the react module */

/* Creates a custom react hook [Naming Convention (useMediaQuery) + uses other built-in react hooks to create a reusuable hook] 
Takes in a query parameter, which we specify is a string by using typescript annotation 
That string is a css media query, essentially providing a set of conditions to match against the the browser's current environemnt 
like viewport size , device orientation, etc */

const useMediaQuery = (query: string) => {
    const [matches, setMatches] = useState<boolean>(false);
    /* UseState initializes a state var called matches with default val false */

    useEffect(() => {
        const media: MediaQueryList = window.matchMedia(query);
        /* Window is a global object in browsers to represent the current browser window or tab 
    matchMedia is a method provided by the window object and returns a media query list */
        /* media which is a MediaQueryList has the result of the media query evaluation */

        if (media.matches !== matches) {
            // media.matches returns a boolean val indicating whether the media query matches the browser environment
            setMatches(media.matches); // if our current state var and media.matches aren't the same then we update the val to media.matches using out setMatches function
        }

        const listener = () => setMatches(media.matches); // function that sets our state var to the bool val returned by media.matches
        window.addEventListener('resize', listener); // adds an event listener to window that calls function whenever the resize event occurs (when size of viewport changes)
        return () => window.removeEventListener('resize', listener); // to prevent a memory leak, we call a cleanup function that removes the event listener that we previously added to the window object
    }, [matches, query]); // Callback function is triggered when either the matches var or query changes

    return matches; // finally return the bool val of the state var
};

export default useMediaQuery; // export the function (default so when we import we don't need to use {})
