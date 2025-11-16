import { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import MDEditor from '@uiw/react-md-editor';
import useFetch from "./useFetch";
import useFetchPost from "./useFetchPost";

const api = process.env.REACT_APP_API_URL;

const Create = () => {
    const history = useHistory();

    const [title, setTitle] = useState('');
    const [value, setValue] = useState();
    const [category, setCategory] = useState("");
    const { data: categories, isCtgPending, ctgError } = useFetch(`${api}/api/categories`);
    const { postData, resData, error, isPending } = useFetchPost();

    const handleTitleChange = (e) => {
        setTitle(e.target.value);
    }

    const handleCateChange = (e) => {
        setCategory(e.target.value);
    };

    useEffect(() => {
        if (categories && categories.length > 0 && category === "") {
            setCategory(categories[0].id);
        }
    }, [categories]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const blog = { title, body: value, category_id: category };
        postData(
            `${api}/api/blogs`, blog
        ).then((res) => {
            if (res && res.code === 0) {
                history.push("/");
            }
        });
    }

    return (
        <div className="create">
            <h2>Add a new blog</h2>
            <form onSubmit={handleSubmit}>
                <div className="nes-field create-input-group">
                    <label>Blog Titile:</label>
                    <input
                        type="text"
                        required
                        value={title}
                        className="nes-input"
                        onChange={handleTitleChange}
                    />
                </div>
                <div className="my-md-editor create-input-group">
                    <label>Blog Body:</label>
                    <div className="container editor-wrapper">
                        <MDEditor
                            value={value}
                            onChange={setValue}
                        />
                    </div>
                </div>
                <div className="create-input-group">
                    <label>Blog Titile:</label>
                    {ctgError && <div>{ctgError}</div>}
                    <div className="nes-select">
                        <select name="cateValue" value={category} onChange={handleCateChange}>
                            {categories && categories.map((cat) => (
                                <option value={cat.id} key={cat.id}>{cat.name}</option>
                            ))}
                        </select>
                    </div>
                </div>
                {error && <div><p className="nes-balloon from-left nes-pointer nes-text is-error">{error}</p></div>}
                {!isPending && <button className="nes-btn is-primary">Add Blog</button>}
                {isPending && <button disabled >Adding Blog...</button>}
            </form>
        </div>
    );
}

export default Create;
