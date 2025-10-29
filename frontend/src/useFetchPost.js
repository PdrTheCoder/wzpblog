import { useState } from "react";

const useFetchPost = () => {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const [isPending, setIsPending] = useState(false);

    const postData = (url, postData) => {
        setIsPending(true);
        setError(null);

        return fetch(url, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(postData),
        }).then((res) => {
            if (!res.ok) {
                throw Error('Failed to post data');
            }
            return res.json();
        }).then((json) => {
            setData(json);
            if (json.code !== 0) {
                setError(json.msg);
            }
            return json;
        }).catch((err) => {
            // if there is any error
            setError(err.message);
            return null
        }).finally(() => {
            setIsPending(false);
        })
    };

    return { postData, data, error, isPending };
}

export default useFetchPost;