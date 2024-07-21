import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectAllCategories, createCategory, updateCategory, deleteCategory } from '../../../store/slices/categoriesSlice';
import { selectAllTags, createTag, updateTag, deleteTag } from '../../../store/slices/tagsSlice';

const EntityManagement = () => {
    const dispatch = useDispatch();
    const categories = useSelector(selectAllCategories);
    const tags = useSelector(selectAllTags);

    const [newCategory, setNewCategory] = useState('');
    const [newTag, setNewTag] = useState('');
    const [editingCategory, setEditingCategory] = useState(null);
    const [editingTag, setEditingTag] = useState(null);

    const handleCategorySubmit = (e) => {
        e.preventDefault();
        if (editingCategory) {
            dispatch(updateCategory({ ...editingCategory, name: newCategory }));
            setEditingCategory(null);
        } else {
            dispatch(createCategory({ name: newCategory }));
        }
        setNewCategory('');
    };

    const handleTagSubmit = (e) => {
        e.preventDefault();
        if (editingTag) {
            dispatch(updateTag({ ...editingTag, name: newTag }));
            setEditingTag(null);
        } else {
            dispatch(createTag({ name: newTag }));
        }
        setNewTag('');
    };

    return (
        <div className="container mx-auto px-4">
            <h2 className="text-2xl font-bold mb-6">Manage Entities</h2>
            <div className="flex">
                <div className="flex-1 mr-4">
                    <h3 className="text-xl font-bold mb-4">Categories</h3>
                    <form onSubmit={handleCategorySubmit} className="mb-4">
                        <input
                            type="text"
                            value={newCategory}
                            onChange={(e) => setNewCategory(e.target.value)}
                            placeholder="Category name"
                            className="mr-2 p-2 border rounded"
                        />
                        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
                            {editingCategory ? 'Update Category' : 'Add Category'}
                        </button>
                    </form>
                    <ul>
                        {categories.map(category => (
                            <li key={category.id} className="flex items-center justify-between mb-2">
                                {category.name}
                                <div>
                                    <button
                                        onClick={() => {
                                            setEditingCategory(category);
                                            setNewCategory(category.name);
                                        }}
                                        className="bg-yellow-500 text-white p-1 rounded mr-2"
                                    >
                                        Edit
                                    </button>
                                    <button
                                        onClick={() => dispatch(deleteCategory(category.id))}
                                        className="bg-red-500 text-white p-1 rounded"
                                    >
                                        Delete
                                    </button>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>
                <div className="flex-1">
                    <h3 className="text-xl font-bold mb-4">Tags</h3>
                    <form onSubmit={handleTagSubmit} className="mb-4">
                        <input
                            type="text"
                            value={newTag}
                            onChange={(e) => setNewTag(e.target.value)}
                            placeholder="Tag name"
                            className="mr-2 p-2 border rounded"
                        />
                        <button type="submit" className="bg-green-500 text-white p-2 rounded">
                            {editingTag ? 'Update Tag' : 'Add Tag'}
                        </button>
                    </form>
                    <ul>
                        {tags.map(tag => (
                            <li key={tag.id} className="flex items-center justify-between mb-2">
                                {tag.name}
                                <div>
                                    <button
                                        onClick={() => {
                                            setEditingTag(tag);
                                            setNewTag(tag.name);
                                        }}
                                        className="bg-yellow-500 text-white p-1 rounded mr-2"
                                    >
                                        Edit
                                    </button>
                                    <button
                                        onClick={() => dispatch(deleteTag(tag.id))}
                                        className="bg-red-500 text-white p-1 rounded"
                                    >
                                        Delete
                                    </button>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default EntityManagement;